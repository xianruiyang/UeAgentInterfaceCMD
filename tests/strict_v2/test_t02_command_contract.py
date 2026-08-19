from __future__ import annotations

import importlib
import json

import pytest


def _generator():
    return importlib.import_module(
        "tools.uai_repository.command_contract_generation"
    )


def _projection() -> dict[str, object]:
    return {
        "schema": "uai.immutable_command_registry.v1",
        "source": {"kind": "cpp_immutable_command_registry"},
        "registry_hash": "sha256:" + "a" * 64,
        "commands": [
            {
                "command_id": "sample.execute",
                "python_namespace": "sample",
                "python_function": "execute",
                "contract_version": 3,
                "contract_hash": "sha256:" + "b" * 64,
                "public_owner": "sample-operation-owner",
                "availability": "enabled",
                "side_effect": "asset_state",
                "state_layers": ["persisted_asset"],
                "input_fields": [
                    {
                        "name": "target",
                        "wire_type": "string",
                        "required": True,
                        "nullable": False,
                        "description": "Stable target identity.",
                    }
                ],
                "result_fields": [
                    {
                        "name": "revision",
                        "wire_type": "string",
                        "required": True,
                        "nullable": False,
                        "description": "Independently read revision.",
                    }
                ],
                "errors": [
                    {
                        "code": "sample_target_missing",
                        "description": "The exact target is absent.",
                    }
                ],
                "purpose": {
                    "summary": "Apply one exact sample operation.",
                    "target": "A stable sample target identity.",
                    "preconditions": ["Target came from public discovery."],
                    "parameter_guidance": "Pass the exact target identity.",
                    "result_guidance": "Returns persisted revision.",
                    "failure_guidance": "Errors are preserved without fallback.",
                    "side_effect_guidance": "Mutates persisted asset state once.",
                    "minimum_example": "sample.execute(target='/Game/Sample.Sample')",
                    "related_flows": ["sample.discover"],
                    "keywords": ["sample", "apply"],
                    "synonyms": ["update sample"],
                },
            }
        ],
    }


def test_cpp_projection_is_the_only_binding_and_document_input() -> None:
    generator = _generator()
    projection = _projection()

    model = generator.load_projection(
        json.dumps(projection, ensure_ascii=False, sort_keys=True)
    )
    assert model.registry_hash == projection["registry_hash"]
    assert [command.command_id for command in model.commands] == [
        "sample.execute"
    ]

    binding = generator.render_python_binding(model, "sample")
    documentation = generator.render_markdown(model, "sample")
    assert "CPP_REGISTRY_HASH = 'sha256:" in binding
    assert "COMMAND_CONTRACT_HASH = 'sha256:" in binding
    assert "execute_exact('sample.execute'" in binding
    assert "sample.execute" in documentation
    assert "sample_target_missing" in documentation
    assert "update sample" in documentation
    assert generator.render_python_binding(model, "sample") == binding
    assert generator.render_markdown(model, "sample") == documentation


@pytest.mark.parametrize(
    ("mutation", "error_code"),
    [
        (lambda item: item.pop("purpose"), "command_projection_incomplete"),
        (
            lambda item: item.update(command_id="sample"),
            "command_projection_identity_invalid",
        ),
        (
            lambda item: item.update(contract_hash="not-a-hash"),
            "command_projection_hash_invalid",
        ),
    ],
)
def test_incomplete_or_non_exact_projection_is_rejected(
    mutation, error_code: str
) -> None:
    generator = _generator()
    projection = _projection()
    mutation(projection["commands"][0])
    with pytest.raises(generator.CommandProjectionError) as caught:
        generator.load_projection(json.dumps(projection))
    assert caught.value.code == error_code


def test_generated_binding_never_executes_synonyms_or_fallbacks() -> None:
    generator = _generator()
    projection = _projection()
    projection["commands"][0]["purpose"]["synonyms"] = [
        "apply sample",
        "modify sample",
    ]
    model = generator.load_projection(json.dumps(projection))
    binding = generator.render_python_binding(model, "sample")

    assert "sample.execute" in binding
    assert "apply sample" not in binding
    assert "modify sample" not in binding
    assert "fallback" not in binding.lower()
    assert "startswith" not in binding.lower()


def test_duplicate_command_or_python_binding_is_rejected() -> None:
    generator = _generator()
    projection = _projection()
    duplicate_id = dict(projection["commands"][0])
    projection["commands"].append(duplicate_id)
    with pytest.raises(generator.CommandProjectionError) as caught:
        generator.load_projection(json.dumps(projection))
    assert caught.value.code == "command_projection_id_duplicate"

    projection = _projection()
    duplicate_binding = dict(projection["commands"][0])
    duplicate_binding["command_id"] = "sample.inspect"
    duplicate_binding["contract_hash"] = "sha256:" + "c" * 64
    projection["commands"].append(duplicate_binding)
    with pytest.raises(generator.CommandProjectionError) as caught:
        generator.load_projection(json.dumps(projection))
    assert caught.value.code == "command_projection_python_binding_duplicate"
