"""Short model-facing custody for one local HJSON workspace."""

from __future__ import annotations

from pathlib import Path, PurePosixPath
import re
from typing import Any, TYPE_CHECKING

from .commands import OMITTED
from .errors import ProtocolError, TransportError, UsageError
from .external_source import ProjectFileHandle
from .local_paths import find_project_root

if TYPE_CHECKING:
    from .result import Result


# Retain the user's ASCII workspace naming policy for UE path compatibility.
_NAME = re.compile(r"^[a-z0-9][a-z0-9_-]*$")


def _validate_name(name: str) -> None:
    if not isinstance(name, str) or not _NAME.fullmatch(name):
        raise UsageError(
            code="workspace_name_invalid",
            message=(
                "workspace name is a short name, not a directory path; "
                "use lowercase letters or digits first, then lowercase letters, digits, underscores or hyphens "
                "(for example name='my_asset'). The SDK creates tmp/uai-workspaces/<name>; "
                "edit files under the returned workspace.path"
            ),
        )


def _finish_hjson_import(client, result, *, recovery_name=None, operation=None):
    """Use existing operation custody while keeping imports as one SDK call."""
    from .result import Result
    from .errors import ServerCommandError

    operation = operation or result.operation
    if operation is None:
        return result
    diagnostics = list(result.diagnostics)
    name = recovery_name or operation.recovery_name

    def collect(observation):
        for diagnostic in observation.diagnostics:
            if diagnostic not in diagnostics:
                diagnostics.append(diagnostic)

    try:
        business = operation.finish_result(on_observation=collect)
        collect(business)
        if operation.released and name is not None:
            client.operation.forget_checkpoint(name)
        business_response = dict(business._machine_response)
        business_response["diagnostics"] = diagnostics
        return client._wrap_result("content_graph.import_workspace", Result(business_response),
                                   allow_operation_handle=False)
    except ServerCommandError as error:
        failed = dict(error.result._machine_response)
        failed["diagnostics"] = diagnostics
        raise ServerCommandError(result=Result(failed)) from error
    except ProtocolError as error:
        if error.code == "operation_command_result_unavailable":
            raise ProtocolError.at_source(code="hjson_import_result_unavailable",
                                message="The import receipt has no command reply.",
                                facts={**error.diagnostic, "stage": "import_receipt",
                                       "recovery_action": f"resume_import:{name}",
                                       "diagnostics": diagnostics}) from error
        error.diagnostic.setdefault("diagnostics", []).extend(diagnostics)
        raise
    except TransportError as error:
        # The submitted mutation may still finish. Do not submit it again or
        # delete custody; recover the same existing operation after transport returns.
        pending = dict(result._machine_response)
        pending["diagnostics"] = diagnostics
        pending["ok"] = False
        pending["error"] = {
            "code": error.code,
            "message": f"Import outcome is pending; resume with client.content_graph.resume_import('{name}')",
            "recovery_action": f"resume_import:{name}",
            "mutation_may_have_started": True,
            "retry_safe": False,
            "diagnostic": {**error.diagnostic, "recovery_action": f"resume_import:{name}",
                           "mutation_may_have_started": True, "retry_safe": False},
        }
        return Result(pending, long_running=True, operation=operation)


class HjsonWorkspaceHandle:
    """Own the absolute machine path while exposing one short relative path."""

    __slots__ = ("_client", "_absolute_path", "_target", "_result", "_path")

    def __init__(
        self,
        client: Any,
        *,
        target: str,
        name: str,
        result: "Result | None" = None,
    ) -> None:
        _validate_name(name)
        root = find_project_root(client._connection.source_path)
        relative = PurePosixPath("tmp") / "uai-workspaces" / name
        self._client = client
        self._absolute_path = (root / Path(relative)).resolve()
        self._target = target
        self._result = result
        self._path = relative

    @property
    def path(self) -> PurePosixPath:
        return self._path

    def __repr__(self) -> str:
        return f"HjsonWorkspaceHandle(path={self._path.as_posix()!r})"

    @property
    def result(self) -> "Result | None":
        """Export result, or None when an existing workspace was opened locally."""
        return self._result

    def scene_context(self, **options) -> "SceneAnalysisHandle":
        """Read proposed changes and their neighborhood using the native import preparation."""
        return self._analyze("world.scene_context", options)

    def geometry_overlap(self, **options) -> "SceneAnalysisHandle":
        """Analyze proposed geometry; does not require scene_context first."""
        return self._analyze("world.geometry_overlap", options)

    def _analyze(self, command: str, options) -> "SceneAnalysisHandle":
        if "workspace_root" in options:
            raise UsageError(code="scene_analysis_workspace_owned", message="The workspace handle owns workspace_root")
        result = self._client.execute(command, {"input": {"workspace_root": str(self._absolute_path), **options}})
        if result.operation is not None:
            result = result.operation.finish_result()
        result.raise_for_error()
        return SceneAnalysisHandle(self._client, result)

    def import_changes(self, *, analysis: "SceneAnalysisHandle | None" = None) -> "Result":
        source = {"kind": "directory", "path": str(self._absolute_path)}
        return self._client._import_hjson_workspace(
            self._target,
            source,
            analysis_ref=analysis._reference if analysis is not None else OMITTED,
        )


class SceneAnalysisHandle:
    """Versioned native analysis. Pages and both projections reuse the same preparation."""

    __slots__ = ("_client", "_reference", "result")

    def __init__(self, client, result):
        self._client = client
        self.result = result
        self._reference = result.payload["analysis"]["analysis_ref"]

    def __repr__(self):
        return "SceneAnalysisHandle(status=%r)" % self.result.payload["analysis"].get("status")

    def _query(self, command, options):
        result = self._client.execute(command, {"input": {**options, "analysis_ref": self._reference}})
        if result.operation is not None:
            result = result.operation.finish_result()
        result.raise_for_error()
        return SceneAnalysisHandle(self._client, result)

    def scene_context(self, **options):
        return self._query("world.scene_context", options)

    def geometry_overlap(self, **options):
        return self._query("world.geometry_overlap", options)


class ContentGraphNamespace:
    """Generated content-graph API with SDK-owned workspace paths."""

    __slots__ = ("_client", "_generated")

    def __init__(self, client: Any, generated: Any) -> None:
        self._client = client
        self._generated = generated

    def export_workspace(
        self,
        target: str,
        *,
        name: str = "current",
        profile_id=OMITTED,
        source=OMITTED,
    ) -> HjsonWorkspaceHandle:
        """Export into SDK-managed tmp/uai-workspaces/<name>; name is not a path."""
        _validate_name(name)
        root = find_project_root(self._client._connection.source_path)
        absolute = (root / "tmp" / "uai-workspaces" / name).resolve()
        result = self._client._export_hjson_workspace(
            target,
            str(absolute),
            profile_id=profile_id,
            source=source,
        )
        return HjsonWorkspaceHandle(
            self._client,
            target=target,
            name=name,
            result=result,
        )

    def open_workspace(
        self,
        target: str,
        *,
        name: str = "current",
    ) -> HjsonWorkspaceHandle:
        """Open an existing directory without export, writes or manifest parsing.

        The server validates target and the saved baseline on import_changes().
        The returned handle has no export result (result is None).
        """
        return HjsonWorkspaceHandle(self._client, target=target, name=name)

    def import_file(
        self,
        target: str,
        source: ProjectFileHandle | str | PurePosixPath,
    ) -> "Result":
        handle = (
            source
            if isinstance(source, ProjectFileHandle)
            else ProjectFileHandle(self._client, source)
        )
        return self._client._import_hjson_workspace(
            target,
            {"kind": "single_file", "path": handle._wire_value()},
        )

    def import_inline(
        self,
        target: str,
        document: str,
    ) -> "Result":
        """Import HJSON or JSON text; serialize Python mappings before calling."""
        return self._client._import_hjson_workspace(
            target,
            {"kind": "inline", "document": document},
        )

    def resume_import(self, recovery_name: str) -> "Result":
        """Get a timed-out import's actual reply without resubmitting its changes."""
        operation = self._client.operation.recover(recovery_name)
        result = operation.receipt() if operation._released else operation.status()
        return _finish_hjson_import(self._client, result, recovery_name=recovery_name, operation=operation)

    def __getattr__(self, name):
        if name == "import_workspace":
            raise AttributeError(
                "use HjsonWorkspaceHandle.import_changes()"
            )
        return getattr(self._generated, name)


__all__ = ["ContentGraphNamespace", "HjsonWorkspaceHandle"]
