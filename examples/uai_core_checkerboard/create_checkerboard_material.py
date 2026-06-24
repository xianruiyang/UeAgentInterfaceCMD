from __future__ import annotations

import argparse
import json
import socket
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
UAI_CMD_ROOT = SCRIPT_DIR.parents[1]
PROJECT_ROOT = UAI_CMD_ROOT.parent
UAI_CLI_PACKAGE_DIR = UAI_CMD_ROOT / "cli"

if str(UAI_CLI_PACKAGE_DIR) not in sys.path:
    sys.path.insert(0, str(UAI_CLI_PACKAGE_DIR))

from uai_core import UaiCore  # noqa: E402


DEFAULT_ASSET_PATH = "/Game/UAI_Demos/Materials/M_UAICore_Checkerboard"
MATERIAL_FOLDER_ROOT = PROJECT_ROOT / "Saved" / "UeAssetFolders" / "MaterialGraph"
RUNTIME_LOG_ROOT = PROJECT_ROOT / "runtimeLogs"


def now_tag() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def material_folder_for_asset(asset_path: str) -> Path:
    relative = asset_path.strip("/")
    if not relative:
        raise ValueError("asset_path must not be empty")
    return MATERIAL_FOLDER_ROOT / Path(relative)


def result_data(result: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(result, dict):
        return {}
    data = result.get("data")
    return data if isinstance(data, dict) else {}


def build_checkerboard_graph(scale: float) -> dict[str, Any]:
    scale_text = f"{scale:.6f}"
    checker_code = (
        "float2 cell = floor(UV); "
        "float checker = frac((cell.x + cell.y) * 0.5) * 2.0; "
        "checker = saturate(checker); "
        "float3 darkColor = float3(0.02, 0.02, 0.02); "
        "float3 lightColor = float3(0.92, 0.92, 0.92); "
        "return lerp(darkColor, lightColor, checker);"
    )
    return {
        "graph": {
            "name": "MaterialGraph",
            "graph_kind": "material_graph",
        },
        "expressions": [
            {
                "id": "expr_texcoord_scaled",
                "expression_class": "/Script/Engine.MaterialExpressionTextureCoordinate",
                "pos": {"x": -520, "y": 0},
                "properties": [
                    {"property_name": "CoordinateIndex", "value_text": "0"},
                    {"property_name": "UnMirrorU", "value_text": "False"},
                    {"property_name": "UnMirrorV", "value_text": "False"},
                    {"property_name": "UTiling", "value_text": scale_text},
                    {"property_name": "VTiling", "value_text": scale_text},
                ],
            },
            {
                "id": "expr_checker_custom",
                "expression_class": "/Script/Engine.MaterialExpressionCustom",
                "pos": {"x": -140, "y": 0},
                "properties": [
                    {"property_name": "Code", "value_text": checker_code},
                    {"property_name": "Desc", "value_text": ""},
                    {"property_name": "Description", "value_text": "UAICore checkerboard"},
                    {"property_name": "OutputType", "value_text": "CMOT_Float3"},
                    {"property_name": "ShowCode", "value_text": "False"},
                ],
                "custom_inputs": [
                    {"name": "UV"},
                ],
            },
        ],
        "edges": [
            {
                "from": {"node": "expr_texcoord_scaled", "output": ""},
                "to": {"node": "expr_checker_custom", "input": "UV"},
            }
        ],
        "root_inputs": [
            {
                "material_property": "BaseColor",
                "from": {"node": "expr_checker_custom", "output": ""},
            }
        ],
    }


def write_material_folder(asset_path: str, scale: float) -> dict[str, Path]:
    asset_name = asset_path.rstrip("/").split("/")[-1]
    folder = material_folder_for_asset(asset_path)
    files = {
        "asset": folder / "asset.json",
        "settings": folder / "settings" / "material.json",
        "parameters": folder / "parameters" / "interface.json",
        "graph": folder / "graphs" / "MaterialGraph.json",
    }

    write_json(
        files["asset"],
        {
            "format_version": 1,
            "asset_kind": "material_graph",
            "asset_path": asset_path,
            "asset_name": asset_name,
            "profile_version": 1,
            "material_subkind": "material",
        },
    )
    write_json(
        files["settings"],
        {
            "properties": [
                {"key": "material_domain", "property_name": "MaterialDomain", "value_text": "MD_Surface"},
                {"key": "blend_mode", "property_name": "BlendMode", "value_text": "BLEND_Opaque"},
                {"key": "shading_model", "property_name": "ShadingModel", "value_text": "MSM_DefaultLit"},
                {"key": "shading_models", "property_name": "ShadingModels", "value_text": "(ShadingModelField=2)"},
                {"key": "two_sided", "property_name": "TwoSided", "value_text": "False"},
                {
                    "key": "use_material_attributes",
                    "property_name": "bUseMaterialAttributes",
                    "value_text": "False",
                },
            ]
        },
    )
    write_json(files["parameters"], {"parameters": []})
    write_json(files["graph"], build_checkerboard_graph(scale))
    return files


def build_commands(asset_path: str, open_editor: bool) -> list[dict[str, Any]]:
    commands: list[dict[str, Any]] = [
        {
            "request_id": "apply-checkerboard-material",
            "command": "material_apply_folder",
            "params": {
                "asset_path": asset_path,
                "create_if_missing": True,
                "compile_after_apply": True,
                "save_after_apply": True,
            },
        },
        {
            "request_id": "compile-checkerboard-material",
            "command": "material_get_compile_log",
            "params": {
                "asset_path": asset_path,
                "compile_before_read": True,
                "severity_filter": "all",
                "max_messages": 64,
            },
        },
        {
            "request_id": "list-checkerboard-expressions",
            "command": "material_list_expressions",
            "params": {"asset_path": asset_path},
        },
        {
            "request_id": "info-checkerboard-material",
            "command": "material_get_info",
            "params": {"asset_path": asset_path},
        },
        {
            "request_id": "export-checkerboard-material",
            "command": "material_export_folder",
            "params": {
                "asset_path": asset_path,
                "clean_output_dir": True,
                "include_validation": True,
            },
        },
    ]
    if open_editor:
        commands.append(
            {
                "request_id": "open-checkerboard-material-editor",
                "command": "material_open_editor",
                "params": {"asset_path": asset_path},
            }
        )
    return commands


def validate_readback(asset_path: str) -> dict[str, Any]:
    graph_path = material_folder_for_asset(asset_path) / "graphs" / "MaterialGraph.json"
    graph = read_json(graph_path)
    expressions = graph.get("expressions")
    root_inputs = graph.get("root_inputs")
    if not isinstance(expressions, list):
        raise RuntimeError(f"readback graph has no expressions array: {graph_path}")
    if not isinstance(root_inputs, list):
        raise RuntimeError(f"readback graph has no root_inputs array: {graph_path}")

    class_names = {
        expression.get("expression_class")
        for expression in expressions
        if isinstance(expression, dict)
    }
    has_texcoord = "/Script/Engine.MaterialExpressionTextureCoordinate" in class_names
    custom_nodes = [
        expression
        for expression in expressions
        if isinstance(expression, dict)
        and expression.get("expression_class") == "/Script/Engine.MaterialExpressionCustom"
    ]
    has_checker_code = any(
        any(
            isinstance(prop, dict)
            and prop.get("property_name") == "Code"
            and "darkColor" in str(prop.get("value_text", ""))
            and "checker" in str(prop.get("value_text", ""))
            for prop in expression.get("properties", [])
        )
        for expression in custom_nodes
    )
    has_base_color = any(
        isinstance(root_input, dict) and root_input.get("material_property") == "BaseColor"
        for root_input in root_inputs
    )

    if not has_texcoord:
        raise RuntimeError("readback graph is missing TextureCoordinate expression")
    if not custom_nodes or not has_checker_code:
        raise RuntimeError("readback graph is missing checkerboard Custom expression")
    if not has_base_color:
        raise RuntimeError("readback graph is missing BaseColor root input")

    return {
        "graph_path": str(graph_path),
        "expression_count": len(expressions),
        "root_input_count": len(root_inputs),
        "has_texcoord": has_texcoord,
        "has_checker_code": has_checker_code,
        "has_base_color": has_base_color,
    }


def run(asset_path: str, scale: float, open_editor: bool) -> dict[str, Any]:
    authored_files = write_material_folder(asset_path, scale)
    client = UaiCore.from_config(require_token=True)
    doctor = client.doctor()
    if not doctor.get("success", False):
        raise RuntimeError("UAI doctor failed")

    commands = build_commands(asset_path, open_editor)
    batch = client.batch(commands, phase_name="uaicore_checkerboard_material")
    batch.raise_for_failure()

    compile_data = result_data(batch.result_by_request_id("compile-checkerboard-material"))
    if int(compile_data.get("error_count", 0) or 0) > 0:
        raise RuntimeError(f"material compile has errors: {compile_data.get('messages', [])}")

    apply_data = result_data(batch.result_by_request_id("apply-checkerboard-material"))
    export_data = result_data(batch.result_by_request_id("export-checkerboard-material"))
    readback_validation = validate_readback(asset_path)

    report = {
        "schema": "ue_agent_interface.uai_core_checkerboard_material.v1",
        "success": True,
        "asset_path": asset_path,
        "scale": scale,
        "open_editor": open_editor,
        "authored_files": {name: str(path) for name, path in authored_files.items()},
        "doctor_success": doctor.get("success", False),
        "manifest_command_count": (client.manifest or {}).get("command_count", 0),
        "batch": {
            "success": batch.success,
            "request_id": batch.request_id,
            "failed_index": batch.failed_index,
            "failed_command": batch.failed_command,
            "failed_error": batch.failed_error,
            "metrics": batch.metrics,
            "command_manifest_validation": batch.command_manifest_validation,
            "command_param_validation": batch.command_param_validation,
            "response": batch.response,
        },
        "apply": {
            "warning_count": apply_data.get("warning_count", 0),
            "warnings": apply_data.get("warnings", []),
        },
        "compile": {
            "error_count": compile_data.get("error_count", 0),
            "warning_count": compile_data.get("warning_count", 0),
            "message_total_count": compile_data.get("message_total_count", 0),
            "messages": compile_data.get("messages", []),
        },
        "export": export_data,
        "readback_validation": readback_validation,
    }

    report_name = f"uai_core_checkerboard_material_{now_tag()}_{socket.gethostname()}.json"
    report_path = RUNTIME_LOG_ROOT / report_name
    write_json(report_path, report)
    report["report_path"] = str(report_path)
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a checkerboard UMaterial through the uai_core Python API.")
    parser.add_argument("--asset-path", default=DEFAULT_ASSET_PATH)
    parser.add_argument("--scale", type=float, default=8.0)
    parser.add_argument("--no-open-editor", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = run(
        asset_path=args.asset_path,
        scale=args.scale,
        open_editor=not args.no_open_editor,
    )
    print(
        json.dumps(
            {
                "success": True,
                "asset_path": report["asset_path"],
                "scale": report["scale"],
                "report_path": report["report_path"],
                "compile": report["compile"],
                "readback_validation": report["readback_validation"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
