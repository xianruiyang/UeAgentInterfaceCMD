from __future__ import annotations

from pathlib import Path
from typing import Any
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands

COMMAND_ID="blueprint.component.candidates"

class _Client:
    def __init__(self): self.calls:list[tuple[str,dict[str,Any],str]]=[]
    def execute_exact(self,command_id,params,*,contract_hash): self.calls.append((command_id,dict(params),contract_hash)); return {"ok":True}
    def execute(self,command_id,params):
        binding=BINDING_CATALOG.find(command_id); assert binding is not None
        return self.execute_exact(command_id,params,contract_hash=binding.binding_hash)

def _binding():
    binding=BINDING_CATALOG.find(COMMAND_ID); assert binding is not None
    assert binding.namespace=="blueprint" and binding.method=="component_candidates"
    assert re.fullmatch(r"sha256:[0-9a-f]{64}",binding.binding_hash)
    return binding

def test_t12_uses_one_default_component_candidate_binding() -> None: _binding()

def test_t12_named_candidate_forwards_exact_identities() -> None:
    client=_Client(); params={"target":"/Game/UAI/StrictV2/T12.BP","component_class":"/Script/Engine.SceneComponent","requested_name":"SceneRoot"}
    bind_generated_commands(client).blueprint.component_candidates(**params)
    assert len(client.calls)==1 and client.calls[0][0]==COMMAND_ID and client.calls[0][1]==params

def test_t12_default_binding_contains_no_scs_business() -> None:
    names=set(bind_generated_commands(_Client()).blueprint.component_candidates.__func__.__code__.co_names)
    assert not {"scs","component","create","compile","save","reload","rollback"}&names

def test_t12_task_projection_registration_and_tutorial_authority_exit() -> None:
    cmd_root=Path(__file__).resolve().parents[2]; project=cmd_root.parent
    assert not (cmd_root/"cli/uai/generated_commands/blueprint_component").exists()
    docs=(cmd_root/"docs/active/t12_blueprint_component.md",project/"Plugins/UeAgentInterface/docs/active/t12_blueprint_component.md")
    for document in docs:
        text=document.read_text(encoding="utf-8")
        assert "client.blueprint.component_candidates" in text
        assert "command_search" in text and "command_detail" in text and "uai-cli" in text
        assert "T13" in text and "recursive" in text and "initialization" in text
        assert "uai.generated_commands" not in text
    registration=(project/"Plugins/UeAgentInterface/Source/UeAgentInterface/Private/Module/CommandRegistration/BlueprintComponent/UeAgentBlueprintComponentRegistration.cpp").read_text(encoding="utf-8")
    assert 'Result.PythonNamespace = TEXT("blueprint")' in registration
    assert 'Result.PythonFunction = TEXT("component_candidates")' in registration
