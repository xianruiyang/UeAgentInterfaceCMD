"""Typed SDK custody for AssetDurable maintenance continuations."""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any, TYPE_CHECKING
import uuid

from .errors import UsageError

if TYPE_CHECKING:
    from .result import Result


class DurableJournalHandle:
    """Own one journal identity and its latest maintenance binding."""

    __slots__ = (
        "_client",
        "_journal_id",
        "_journal_owner_id",
        "_fencing_token",
    )

    def __repr__(self) -> str:
        return "DurableJournalHandle()"

    def __init__(self, client: Any, journal_id: str) -> None:
        if not isinstance(journal_id, str) or not journal_id.strip():
            raise UsageError(
                code="asset_durable_journal_invalid",
                message="durable journal custody is incomplete",
            )
        self._client = client
        self._journal_id = journal_id
        self._journal_owner_id: str | None = None
        self._fencing_token: int | None = None

    def _update(self, result: "Result") -> "Result":
        payload = result._machine_payload
        if isinstance(payload, Mapping):
            owner = payload.get("journal_owner_id")
            fence = payload.get("fencing_token")
            if isinstance(owner, str) and owner.strip():
                self._journal_owner_id = owner
            if isinstance(fence, int) and not isinstance(fence, bool):
                self._fencing_token = fence
        return result

    def inspect(self) -> "Result":
        return self._update(
            self._client._execute_asset_durable(
                "asset_durable.journal.read",
                {"journal_id": self._journal_id},
                handle=self,
            )
        )

    def reconcile(self) -> "Result":
        if self._journal_owner_id is None or self._fencing_token is None:
            inspected = self.inspect()
            if not inspected.ok:
                return inspected
        if self._journal_owner_id is None or self._fencing_token is None:
            raise UsageError.at_source(
                code="asset_durable_binding_missing",
                message="durable journal inspection did not establish a binding",
                facts={"stage": "journal_inspect", "recovery_action": "inspect_journal"},
            )
        result = self._client._execute_asset_durable(
            "asset_durable.journal.reconcile",
            {
                "journal_id": self._journal_id,
                "expected_journal_owner_id": self._journal_owner_id,
                "expected_fencing_token": self._fencing_token,
                "verification_id": f"sdk-maintenance-{uuid.uuid4()}",
            },
            handle=self,
        )
        return self._update(result)


def _collect_journal_ids(value: object) -> tuple[str, ...]:
    found: list[str] = []

    def visit(item: object) -> None:
        if isinstance(item, Mapping):
            journal_id = item.get("journal_id")
            if (
                isinstance(journal_id, str)
                and journal_id.strip()
                and journal_id not in found
            ):
                found.append(journal_id)
            for child in item.values():
                visit(child)
        elif isinstance(item, (list, tuple)):
            for child in item:
                visit(child)

    visit(value)
    return tuple(found)


class AssetDurableNamespace:
    """Public namespace that accepts Results, never raw journal identities."""

    __slots__ = ("_client",)

    def __init__(self, client: Any) -> None:
        self._client = client

    def from_result(self, result: "Result") -> tuple[DurableJournalHandle, ...]:
        handles = result.durable_journals
        if not handles:
            raise UsageError(
                code="asset_durable_journal_missing",
                message="result does not contain durable recovery custody",
            )
        return handles


def _from_payload(client: Any, payload: object) -> tuple[DurableJournalHandle, ...]:
    return tuple(
        DurableJournalHandle(client, journal_id)
        for journal_id in _collect_journal_ids(deepcopy(payload))
    )


__all__ = ["AssetDurableNamespace", "DurableJournalHandle"]
