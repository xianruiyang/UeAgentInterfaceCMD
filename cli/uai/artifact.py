"""Typed custody for file artifacts returned by UAI operations."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path, PurePosixPath
import shutil
from typing import Any, Literal

from .errors import ProtocolError, UsageError
from .external_source import ProjectFileHandle
from .local_paths import find_project_root


def _materialize_failure(exc: OSError, *, phase: str, destination: PurePosixPath) -> UsageError:
    facts: dict[str, object] = {
        "phase": phase, "property_path": "destination", "target": str(destination),
        "exception_type": type(exc).__name__,
        "recovery_action": "retry materialize; the original artifact remains available",
    }
    for name in ("errno", "winerror"):
        value = getattr(exc, name, None)
        if isinstance(value, int):
            facts[name] = value
    return UsageError.at_source(
        code="artifact_materialize_failed",
        message=f"Local artifact save failed during {phase}: {exc.strerror or type(exc).__name__}.",
        facts=facts,
    )


class ArtifactHandle:
    """Own a machine locator and expose only explicit short materialization."""

    __slots__ = ("_absolute_path", "_byte_count", "_client", "_media_type")

    def __init__(
        self,
        client: Any,
        *,
        locator: str,
        media_type: str | None = None,
        byte_count: int | None = None,
    ) -> None:
        if not isinstance(locator, str) or not locator.strip():
            raise UsageError.at_source(
                code="artifact_locator_invalid",
                message="artifact locator must be a non-empty string",
                facts={"property_path": "locator", "expected_value": "non-empty string", "actual_type": type(locator).__name__},
            )
        self._client = client
        source = Path(locator).expanduser()
        if not source.is_absolute():
            source = find_project_root(client._connection.source_path) / source
        self._absolute_path = source.resolve()
        self._media_type = media_type if isinstance(media_type, str) else None
        self._byte_count = (
            byte_count
            if isinstance(byte_count, int) and not isinstance(byte_count, bool)
            else None
        )

    @property
    def media_type(self) -> str | None:
        return self._media_type

    @property
    def byte_count(self) -> int | None:
        return self._byte_count

    def __repr__(self) -> str:
        return (
            "ArtifactHandle("
            f"media_type={self._media_type!r}, byte_count={self._byte_count!r})"
        )

    def materialize(
        self,
        destination: str | PurePosixPath,
        *,
        on_conflict: Literal["rename", "error"] = "rename",
    ) -> ProjectFileHandle:
        """Reuse identical bytes or copy without overwrite; return the actual path.

        By default a different existing file selects a numbered sibling. Use
        on_conflict="error" when the exact destination is required. Failure only
        affects this local copy: the operation and its artifact remain available.
        """

        if on_conflict not in ("rename", "error"):
            raise UsageError.at_source(code="artifact_conflict_policy_invalid",
                                      message="on_conflict must be rename or error",
                                      facts={"property_path": "on_conflict", "expected_value": ["rename", "error"],
                                             **({"actual_value": on_conflict} if isinstance(on_conflict, str)
                                                else {"actual_type": type(on_conflict).__name__})})
        target = ProjectFileHandle(self._client, destination)
        requested_relative = target.path
        requested = Path(target._wire_value())
        phase = "inspect_source"
        try:
            if not self._absolute_path.is_file():
                raise UsageError.at_source(
                    code="artifact_source_missing",
                    message="artifact source is not an available local file",
                    facts={"phase": phase, "property_path": "artifact", "expected_value": "existing file"},
                )
            phase = "create_destination_directory"
            requested.parent.mkdir(parents=True, exist_ok=True)
            index = 0
            while True:
                output = requested if index == 0 else requested.with_name(
                    f"{requested.stem}-{index}{requested.suffix}")
                target = ProjectFileHandle(self._client, requested_relative.with_name(output.name))
                phase = "open_destination"
                try:
                    stream = output.open("xb")
                except OSError:
                    phase = "compare_existing_destination"
                    # Windows reports an existing directory as PermissionError.
                    if not output.exists() and not output.is_symlink():
                        raise
                    if output.is_file() and _same_content(self._absolute_path, output):
                        return target
                    if on_conflict == "error":
                        raise UsageError.at_source(
                            code="artifact_destination_exists",
                            message="destination contains different content; save this same artifact "
                                    "to another path or use on_conflict='rename'; do not rerun the operation",
                            facts={"property_path": "destination", "target": str(target.path), "on_conflict": on_conflict},
                        ) from None
                    index += 1
                    continue
                try:
                    phase = "copy_artifact"
                    with stream, self._absolute_path.open("rb") as source:
                        shutil.copyfileobj(source, stream)
                except BaseException as copy_exc:
                    # Remove only the incomplete file exclusively created here.
                    try:
                        output.unlink(missing_ok=True)
                    except OSError as cleanup_exc:
                        if isinstance(copy_exc, OSError):
                            failure = _materialize_failure(copy_exc, phase=phase, destination=target.path)
                            failure.diagnostic["diagnostics"] = [
                                _materialize_failure(cleanup_exc, phase="remove_incomplete_copy", destination=target.path).diagnostic
                            ]
                            raise failure from None
                        raise copy_exc from cleanup_exc
                    raise
                return target
        except OSError as exc:
            raise _materialize_failure(exc, phase=phase, destination=target.path) from None


def _same_content(source: Path, destination: Path) -> bool:
    """Compare bytes, not timestamps or a stale cross-call file comparison cache."""
    if source.stat().st_size != destination.stat().st_size:
        return False
    with source.open("rb") as left, destination.open("rb") as right:
        while True:
            block = left.read(1024 * 1024)
            if block != right.read(1024 * 1024):
                return False
            if not block:
                return True


def _from_payload(client: Any, payload: object) -> tuple[ArtifactHandle, ...]:
    found: list[ArtifactHandle] = []
    locators: set[str] = set()

    def visit(value: object) -> None:
        if isinstance(value, Mapping):
            locator = value.get("locator")
            if (
                isinstance(locator, str)
                and locator.strip()
                and locator not in locators
                and any(
                    field in value
                    for field in (
                        "artifact_id",
                        "artifact_ref",
                        "byte_count",
                        "content_hash",
                        "media_type",
                        "mime_type",
                    )
                )
            ):
                locators.add(locator)
                found.append(
                    ArtifactHandle(
                        client,
                        locator=locator,
                        media_type=(
                            value.get("media_type") or value.get("mime_type")
                        ),
                        byte_count=value.get("byte_count"),
                    )
                )
            for child in value.values():
                visit(child)
        elif isinstance(value, (list, tuple)):
            for child in value:
                visit(child)

    visit(payload)
    return tuple(found)


def _roles_from_payload(
    payload: object, artifacts: tuple[ArtifactHandle, ...]
) -> tuple[ArtifactHandle | None, tuple[ArtifactHandle, ...]]:
    """Resolve explicit artifact roles without assigning meaning to traversal order."""
    if not artifacts or not isinstance(payload, Mapping):
        return None, ()
    owner = payload
    signal = payload.get("latest_signal")
    if isinstance(signal, Mapping) and isinstance(signal.get("payload"), Mapping):
        owner = signal["payload"]
    by_path = {artifact._absolute_path: artifact for artifact in artifacts}

    def resolve(reference: object, pointer: str) -> ArtifactHandle:
        locator = reference.get("locator") if isinstance(reference, Mapping) else None
        if isinstance(locator, str) and locator.strip():
            path = Path(locator).expanduser()
            if not path.is_absolute():
                path = find_project_root(artifacts[0]._client._connection.source_path) / path
            handle = by_path.get(path.resolve())
            if handle is not None:
                return handle
        raise ProtocolError.at_source(
            code="artifact_role_reference_invalid",
            message="The declared artifact role does not identify an available artifact.",
            facts={"json_pointer": pointer, "expected_value": "available artifact reference"},
        )

    # Some non-capture responses use artifact_ref as a scalar identifier on a
    # descriptor. Only a reference object declares the primary-output role.
    primary_ref = owner.get("artifact_ref")
    primary = resolve(primary_ref, "/artifact_ref") if isinstance(primary_ref, Mapping) else None
    references = owner.get("additional_artifact_refs", ())
    if not isinstance(references, (list, tuple)):
        raise ProtocolError.at_source(
            code="artifact_role_reference_invalid",
            message="Additional artifact references must be an ordered array.",
            facts={"json_pointer": "/additional_artifact_refs", "expected_value": "array"},
        )
    additional = tuple(resolve(reference, f"/additional_artifact_refs/{index}")
                       for index, reference in enumerate(references))
    return primary, additional


__all__ = ["ArtifactHandle"]
