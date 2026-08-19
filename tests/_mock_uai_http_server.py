from __future__ import annotations

import json
import queue
import sys
import threading
import time
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any


@dataclass(slots=True)
class MockUaiRequest:
    method: str
    path: str
    payload: dict[str, Any]


@dataclass(slots=True)
class MockUaiState:
    status_data: dict[str, Any]
    status_delay_seconds: float = 0.0
    requests: list[MockUaiRequest] = field(default_factory=list)
    lock: threading.Lock = field(default_factory=threading.Lock)

    def record(self, method: str, path: str, payload: dict[str, Any] | None = None) -> None:
        with self.lock:
            self.requests.append(MockUaiRequest(method, path, payload or {}))

    def count(self, method: str, path: str) -> int:
        with self.lock:
            return sum(item.method == method and item.path == path for item in self.requests)

    def clear_requests(self) -> None:
        with self.lock:
            self.requests.clear()

    def update_status(self, **fields: Any) -> None:
        with self.lock:
            self.status_data.update(fields)

    def status_payload(self) -> dict[str, Any]:
        with self.lock:
            return {"ok": True, "data": dict(self.status_data)}


class _ReusableThreadingHttpServer(ThreadingHTTPServer):
    allow_reuse_address = True
    daemon_threads = False
    block_on_close = True

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.background_errors: queue.Queue[tuple[BaseException, Any]] = queue.Queue()

    def handle_error(self, request: Any, client_address: Any) -> None:
        error = sys.exc_info()[1]
        if error is not None:
            self.background_errors.put((error, error.__traceback__))


class _Handler(BaseHTTPRequestHandler):
    server: _ReusableThreadingHttpServer

    def log_message(self, format: str, *args: object) -> None:
        return

    @property
    def state(self) -> MockUaiState:
        return self.server.mock_state  # type: ignore[attr-defined]

    def do_GET(self) -> None:
        self.state.record("GET", self.path)
        if self.path == "/api/ping":
            self._write_json({"ok": True, "data": {}})
            return
        if self.path == "/api/status":
            if self.state.status_delay_seconds > 0:
                time.sleep(self.state.status_delay_seconds)
            self._write_json(self.state.status_payload())
            return
        self._write_json({"ok": False, "error": "not_found"}, status=404)

    def do_POST(self) -> None:
        content_length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(content_length) if content_length else b"{}"
        payload = json.loads(raw.decode("utf-8"))
        self.state.record("POST", self.path, payload)
        if self.path != "/api/exec":
            self._write_json({"ok": False, "error": "not_found"}, status=404)
            return

        command = str(payload.get("command") or "")
        data = self._command_data(command, payload.get("params", {}))
        self._write_json({"ok": True, "error": "", "data": data})

    @staticmethod
    def _command_data(command: str, params: Any) -> dict[str, Any]:
        if command == "get_world_state":
            return {"map_name": "MockMap", "package_name": "/Game/Maps/MockMap", "dirty": False}
        if command == "list_actors":
            return {"actors": [], "count": 0}
        if command == "material_apply_folder":
            return {
                "asset_path": str(params.get("asset_path") or ""),
                "saved": True,
                "status": "applied",
            }
        if command == "material_export_folder":
            return {
                "asset_path": str(params.get("asset_path") or ""),
                "folder_path": ".",
                "file_count": 1,
                "written_files": ["index.hjson"],
                "status": "written",
            }
        if command == "material_get_info":
            return {"asset_path": str(params.get("asset_path") or ""), "expression_count": 1}
        return {"command": command}

    def _write_json(self, payload: dict[str, Any], *, status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        try:
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError):
            return


class MockUaiHttpServer:
    def __init__(self, status_data: dict[str, Any], *, port: int = 0) -> None:
        self.state = MockUaiState(dict(status_data))
        self.port = port
        self._server: _ReusableThreadingHttpServer | None = None
        self._thread: threading.Thread | None = None

    @property
    def base_url(self) -> str:
        if not self.port:
            raise RuntimeError("mock server is not started")
        return f"http://127.0.0.1:{self.port}"

    def start(self) -> None:
        if self._server is not None:
            raise RuntimeError("mock server is already started")
        server = _ReusableThreadingHttpServer(("127.0.0.1", self.port), _Handler)
        server.mock_state = self.state  # type: ignore[attr-defined]
        self.port = int(server.server_address[1])
        self._server = server
        self._thread = threading.Thread(target=server.serve_forever, daemon=True)
        self._thread.start()

    def stop(self, *, raise_background: bool = True) -> None:
        server = self._server
        if server is None:
            return
        server.shutdown()
        server.server_close()
        if self._thread is not None:
            self._thread.join(timeout=5.0)
        self._server = None
        self._thread = None
        if raise_background and not server.background_errors.empty():
            error, traceback = server.background_errors.get_nowait()
            raise error.with_traceback(traceback)

    def __enter__(self) -> MockUaiHttpServer:
        self.start()
        return self

    def __exit__(self, exc_type, exc, traceback) -> None:
        self.stop(raise_background=exc is None)
