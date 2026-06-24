from __future__ import annotations

import argparse
import json
import shutil
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

OLD_ASSET_PATH = "/Game/UAI_Demos/Materials/M_UAICore_Checkerboard"
NEW_ASSET_PATH = "/Game/UAI_Demos/Materials/M_UAICore_HexPackedDots"
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


def safe_remove_material_folder(asset_path: str) -> bool:
    folder = material_folder_for_asset(asset_path).resolve()
    root = MATERIAL_FOLDER_ROOT.resolve()
    if folder == root or root not in folder.parents:
        raise RuntimeError(f"refusing to remove unsafe folder: {folder}")
    if not folder.exists():
        return False
    shutil.rmtree(folder)
    return True


def build_hex_dots_graph(scale: float, radius: float, feather: float) -> dict[str, Any]:
    scale_text = f"{scale:.6f}"
    radius_text = f"{radius:.6f}"
    feather_text = f"{feather:.6f}"
    code = (
        "float sqrt3 = 1.73205080757; "
        "float2 p = UV; "
        "float2 q = float2(p.x - p.y / sqrt3, p.y * 2.0 / sqrt3); "
        "float2 baseCell = floor(q); "
        "float minDist = 10000.0; "
        "for (int ix = -1; ix <= 1; ++ix) { "
        "for (int iy = -1; iy <= 1; ++iy) { "
        "float2 lattice = baseCell + float2(ix, iy); "
        "float2 center = float2(lattice.x + 0.5 * lattice.y, 0.86602540378 * lattice.y); "
        "minDist = min(minDist, length(p - center)); "
        "} } "
        f"float dotMask = 1.0 - smoothstep({radius_text}, {radius_text} + {feather_text}, minDist); "
        "float3 baseColor = float3(0.045, 0.055, 0.065); "
        "float3 dotColor = float3(0.95, 0.84, 0.24); "
        "float3 rimColor = float3(1.0, 0.98, 0.72); "
        f"float rim = 1.0 - smoothstep({radius_text} * 0.72, {radius_text}, minDist); "
        "float3 circleColor = lerp(dotColor, rimColor, rim * 0.28); "
        "return lerp(baseColor, circleColor, dotMask);"
    )
    return {
        "graph": {"name": "MaterialGraph", "graph_kind": "material_graph"},
        "expressions": [
            {
                "id": "expr_hex_uv",
                "expression_class": "/Script/Engine.MaterialExpressionTextureCoordinate",
                "pos": {"x": -540, "y": 0},
                "properties": [
                    {"property_name": "CoordinateIndex", "value_text": "0"},
                    {"property_name": "UnMirrorU", "value_text": "False"},
                    {"property_name": "UnMirrorV", "value_text": "False"},
                    {"property_name": "UTiling", "value_text": scale_text},
                    {"property_name": "VTiling", "value_text": scale_text},
                ],
            },
            {
                "id": "expr_hex_dots_custom",
                "expression_class": "/Script/Engine.MaterialExpressionCustom",
                "pos": {"x": -140, "y": 0},
                "properties": [
                    {"property_name": "Code", "value_text": code},
                    {"property_name": "Desc", "value_text": ""},
                    {"property_name": "Description", "value_text": "UAICore hex packed circular dots"},
                    {"property_name": "OutputType", "value_text": "CMOT_Float3"},
                    {"property_name": "ShowCode", "value_text": "False"},
                ],
                "custom_inputs": [{"name": "UV"}],
            },
        ],
        "edges": [
            {
                "from": {"node": "expr_hex_uv", "output": ""},
                "to": {"node": "expr_hex_dots_custom", "input": "UV"},
            }
        ],
        "root_inputs": [
            {"material_property": "BaseColor", "from": {"node": "expr_hex_dots_custom", "output": ""}}
        ],
    }


def write_material_folder(asset_path: str, scale: float, radius: float, feather: float) -> dict[str, Path]:
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
                {"key": "use_material_attributes", "property_name": "bUseMaterialAttributes", "value_text": "False"},
            ]
        },
    )
    write_json(files["parameters"], {"parameters": []})
    write_json(files["graph"], build_hex_dots_graph(scale, radius, feather))
    return files


def delete_old_asset(ue: UaiCore, asset_path: str) -> dict[str, Any]:
    dry_params = {
        "asset_path": asset_path,
        "dry_run": True,
        "allow_dirty": True,
        "close_asset_editors": True,
        "allow_open_editors": False,
        "include_path_string_hits": False,
        "fail_on_blocked": False,
    }
    dry = ue.exec("asset_delete", dry_params, request_id="dry-delete-old-checkerboard")
    delete_result: dict[str, Any] | None = None
    dry_data = dry.response.get("data") if isinstance(dry.response, dict) else {}
    deletable_count = int((dry_data or {}).get("deletable_count", 0) or 0) if isinstance(dry_data, dict) else 0
    if dry.success and deletable_count > 0:
        delete_params = dict(dry_params)
        delete_params["dry_run"] = False
        actual = ue.exec("asset_delete", delete_params, request_id="delete-old-checkerboard")
        actual.raise_for_failure()
        delete_result = actual.response
    removed_folder = safe_remove_material_folder(asset_path)
    return {
        "dry_run_success": dry.success,
        "dry_run_response": dry.response,
        "delete_response": delete_result,
        "removed_material_folder": removed_folder,
    }


def validate_readback(asset_path: str) -> dict[str, Any]:
    graph_path = material_folder_for_asset(asset_path) / "graphs" / "MaterialGraph.json"
    graph = read_json(graph_path)
    expressions = graph.get("expressions")
    root_inputs = graph.get("root_inputs")
    if not isinstance(expressions, list):
        raise RuntimeError("readback graph has no expressions array")
    if not isinstance(root_inputs, list):
        raise RuntimeError("readback graph has no root_inputs array")
    classes = {expr.get("expression_class") for expr in expressions if isinstance(expr, dict)}
    custom_nodes = [
        expr
        for expr in expressions
        if isinstance(expr, dict) and expr.get("expression_class") == "/Script/Engine.MaterialExpressionCustom"
    ]
    has_hex_code = any(
        any(
            isinstance(prop, dict)
            and prop.get("property_name") == "Code"
            and "sqrt3" in str(prop.get("value_text", ""))
            and "lattice" in str(prop.get("value_text", ""))
            and "dotMask" in str(prop.get("value_text", ""))
            for prop in expr.get("properties", [])
        )
        for expr in custom_nodes
    )
    has_base_color = any(
        isinstance(root_input, dict) and root_input.get("material_property") == "BaseColor"
        for root_input in root_inputs
    )
    if "/Script/Engine.MaterialExpressionTextureCoordinate" not in classes:
        raise RuntimeError("missing TextureCoordinate expression")
    if not has_hex_code:
        raise RuntimeError("missing hex packed dot Custom expression")
    if not has_base_color:
        raise RuntimeError("missing BaseColor root input")
    return {
        "graph_path": str(graph_path),
        "expression_count": len(expressions),
        "root_input_count": len(root_inputs),
        "has_texture_coordinate": True,
        "has_hex_dot_code": True,
        "has_base_color": True,
    }


def run(scale: float, radius: float, feather: float, open_editor: bool) -> dict[str, Any]:
    authored_files = write_material_folder(NEW_ASSET_PATH, scale, radius, feather)
    ue = UaiCore.from_config(require_token=True)
    doctor = ue.doctor()
    if not doctor.get("success", False):
        raise RuntimeError("UAI doctor failed")
    delete_report = delete_old_asset(ue, OLD_ASSET_PATH)
    commands: list[dict[str, Any]] = [
        {
            "request_id": "apply-hex-packed-dots-material",
            "command": "material_apply_folder",
            "params": {
                "asset_path": NEW_ASSET_PATH,
                "create_if_missing": True,
                "compile_after_apply": True,
                "save_after_apply": True,
            },
        },
        {
            "request_id": "compile-hex-packed-dots-material",
            "command": "material_get_compile_log",
            "params": {
                "asset_path": NEW_ASSET_PATH,
                "compile_before_read": True,
                "severity_filter": "all",
                "max_messages": 64,
            },
        },
        {
            "request_id": "list-hex-packed-dots-expressions",
            "command": "material_list_expressions",
            "params": {"asset_path": NEW_ASSET_PATH},
        },
        {
            "request_id": "export-hex-packed-dots-material",
            "command": "material_export_folder",
            "params": {
                "asset_path": NEW_ASSET_PATH,
                "clean_output_dir": True,
                "include_validation": True,
            },
        },
    ]
    if open_editor:
        commands.append(
            {
                "request_id": "open-hex-packed-dots-material-editor",
                "command": "material_open_editor",
                "params": {"asset_path": NEW_ASSET_PATH},
            }
        )
    commands.extend(
        [
            {
                "request_id": "save-hex-packed-dots-after-open",
                "command": "editor_resolve_dirty_resources",
                "params": {
                    "save_resource_paths": [NEW_ASSET_PATH],
                    "discard_resource_paths": [],
                    "save_all_dirty": False,
                    "discard_all_dirty": False,
                    "close_all_asset_editors": False,
                    "only_save_dirty": True,
                },
            },
            {
                "request_id": "dirty-check-hex-packed-dots",
                "command": "editor_list_dirty_resources",
                "params": {},
            },
        ]
    )
    batch = ue.batch(commands, phase_name="uaicore_hex_packed_dots_material")
    batch.raise_for_failure()
    compile_data = result_data(batch.result_by_request_id("compile-hex-packed-dots-material"))
    if int(compile_data.get("error_count", 0) or 0) > 0:
        raise RuntimeError(f"material compile has errors: {compile_data.get('messages', [])}")
    dirty_data = result_data(batch.result_by_request_id("dirty-check-hex-packed-dots"))
    dirty_matches = [
        item
        for item in dirty_data.get("dirty_resources", [])
        if isinstance(item, dict) and item.get("asset_path") == NEW_ASSET_PATH
    ]
    readback_validation = validate_readback(NEW_ASSET_PATH)
    report = {
        "schema": "ue_agent_interface.uai_core_hex_packed_dots_material.v1",
        "success": len(dirty_matches) == 0,
        "old_asset_path": OLD_ASSET_PATH,
        "new_asset_path": NEW_ASSET_PATH,
        "scale": scale,
        "radius": radius,
        "feather": feather,
        "open_editor": open_editor,
        "authored_files": {name: str(path) for name, path in authored_files.items()},
        "doctor_success": doctor.get("success", False),
        "delete_old_asset": delete_report,
        "batch": {
            "success": batch.success,
            "request_id": batch.request_id,
            "failed_index": batch.failed_index,
            "failed_command": batch.failed_command,
            "failed_error": batch.failed_error,
            "command_manifest_validation": batch.command_manifest_validation,
            "command_param_validation": batch.command_param_validation,
            "metrics": batch.metrics,
            "response": batch.response,
        },
        "compile": {
            "error_count": compile_data.get("error_count", 0),
            "warning_count": compile_data.get("warning_count", 0),
            "message_total_count": compile_data.get("message_total_count", 0),
            "messages": compile_data.get("messages", []),
        },
        "dirty_match_count_after_save": len(dirty_matches),
        "readback_validation": readback_validation,
    }
    report_path = RUNTIME_LOG_ROOT / f"uai_core_hex_packed_dots_material_{now_tag()}_{socket.gethostname()}.json"
    write_json(report_path, report)
    report["report_path"] = str(report_path)
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Replace the checkerboard material with a hex-packed circular dots material.")
    parser.add_argument("--scale", type=float, default=12.0)
    parser.add_argument("--radius", type=float, default=0.31)
    parser.add_argument("--feather", type=float, default=0.035)
    parser.add_argument("--no-open-editor", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = run(
        scale=args.scale,
        radius=args.radius,
        feather=args.feather,
        open_editor=not args.no_open_editor,
    )
    print(json.dumps({
        "success": report["success"],
        "deleted_old_asset": report["delete_old_asset"].get("delete_response") is not None,
        "removed_old_material_folder": report["delete_old_asset"].get("removed_material_folder", False),
        "new_asset_path": report["new_asset_path"],
        "compile": report["compile"],
        "dirty_match_count_after_save": report["dirty_match_count_after_save"],
        "readback_validation": report["readback_validation"],
        "report_path": report["report_path"],
    }, ensure_ascii=False, indent=2))
    return 0 if report["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())