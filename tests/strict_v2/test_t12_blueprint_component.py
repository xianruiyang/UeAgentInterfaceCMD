from __future__ import annotations

from pathlib import Path
from typing import Any
import re

from uai.commands import _BINDING_CATALOG, bind_generated_commands

COMMAND_ID="blueprint.component.candidates"

class _Client:
    def __init__(self): self.calls:list[tuple[str,dict[str,Any],str]]=[]
    def execute_exact(self,command_id,params,*,contract_hash): self.calls.append((command_id,dict(params),contract_hash)); return {"ok":True}
    def execute(self,command_id,params):
        binding=_BINDING_CATALOG.find(command_id); assert binding is not None
        return self.execute_exact(command_id,params,contract_hash=binding.binding_hash)

def _binding():
    binding=_BINDING_CATALOG.find(COMMAND_ID); assert binding is not None
    assert binding.namespace=="blueprint" and binding.method=="component_candidates"
    assert re.fullmatch(r"sha256:[0-9a-f]{64}",binding.binding_hash)
    return binding

