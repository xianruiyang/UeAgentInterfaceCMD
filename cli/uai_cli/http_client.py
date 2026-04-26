from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass
from urllib import error, request

from .errors import HttpError


@dataclass(slots=True)
class HttpResult:
    payload: dict
    elapsed_ms: float
    status_code: int


class UaiHttpClient:
    def __init__(self, base_url: str, token: str, timeout_seconds: int) -> None:
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout_seconds = timeout_seconds

    def get(self, path: str) -> HttpResult:
        url = f"{self.base_url}{path}"
        req = request.Request(url=url, method="GET")
        req.add_header("X-UeAgentInterface-Token", self.token)
        return self._send(req)

    def post_json(self, path: str, payload: dict) -> HttpResult:
        url = f"{self.base_url}{path}"
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        req = request.Request(url=url, method="POST", data=body)
        req.add_header("X-UeAgentInterface-Token", self.token)
        req.add_header("Content-Type", "application/json")
        return self._send(req)

    def _send(self, req: request.Request) -> HttpResult:
        started = time.perf_counter()
        try:
            with request.urlopen(req, timeout=self.timeout_seconds) as response:
                raw = response.read().decode("utf-8")
                payload = json.loads(raw) if raw else {}
                elapsed_ms = (time.perf_counter() - started) * 1000
                return HttpResult(payload=payload, elapsed_ms=elapsed_ms, status_code=response.status)
        except error.HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="ignore")
            payload = {}
            try:
                payload = json.loads(raw) if raw else {}
            except json.JSONDecodeError:
                payload = {"raw": raw}
            raise HttpError(f"HTTP {exc.code}: {payload}", status_code=exc.code, payload=payload) from exc
        except error.URLError as exc:
            raise HttpError(f"网络错误: {exc}") from exc
        except TimeoutError as exc:
            raise HttpError("请求超时") from exc
        except json.JSONDecodeError as exc:
            logging.exception("响应 JSON 解析失败")
            raise HttpError(f"响应 JSON 解析失败: {exc}") from exc

