# UeAgentInterfaceCMD

`UeAgentInterfaceCMD` 是 `UeAgentInterface` 的外置命令行工具与 Python core 库目录。
目标是通过 `uai_core` 复用执行逻辑，并通过 `uai-cli` 提供兼容命令行入口，减少重复输入、提高稳定性和可追踪性。

它与 `UeAgentInterface` 插件仓库配套使用：插件运行在 UE Editor 内，`uai_core` 负责配置、HTTP、manifest 校验、batch/run、report 和失败现场等库逻辑；`uai_cli` 只负责命令行参数解析和子命令分发。

## 代码来源说明

本仓库的初步代码是使用 GPT 编写，并在实际 Unreal Engine 自动化工作流中持续调试、测试和修复。后续维护应以 CLI 单测、UAI 报告、UE 编译/运行验证和文档同步为准。

## 当前重点

- Python core：`uai_core.UaiCore` 可直接用于脚本调用
- 统一入口：`dist/uai-cli.exe`
- 推荐模式：`run`（plan + vars）与 `batch`（JSON 文件）
- 命名简化：内置 `namegen`，默认生成短资产名
- Niagara 护栏：自动 preflight + 编译/日志/emitter 校验
- 自动清理：`tmp/reports` 超阈值自动裁剪
- 命令清单：`manifest` 生成插件命令 manifest，并在执行前校验命令名和废弃生命周期
- 参数校验：manifest 中包含轻量 `param_schema`，支持 warn/strict；高频必填参数和常见别名错误会在 preflight 阶段直接阻断
- 兼容检查：`compat` 检查 CLI 与 UE 插件服务状态
- 失败现场：执行失败自动写入 `runtimeLogs/crashes/<run_id>/`
- 失败复现：`crash signature|replay|bisect`
- Golden E2E：`e2e local|ue-readonly`
- 发布验证：`release coverage|pak-verify|examples|gate|all`

## 快速开始

```powershell
.\dist\uai-cli.exe doctor --json-output
.\dist\uai-cli.exe run --plan ".\plans\sample_plan_list_actors.json" --vars ".\vars\sample_vars.json" --json-output
.\dist\uai-cli.exe manifest --summary --json-output
.\dist\uai-cli.exe release all --json-output
.\dist\uai-cli.exe release gate --json-output
```

Python 侧可直接复用 core：

```python
from uai_core import UaiCore

ue = UaiCore.from_config()
world = ue.exec("get_world_state")
world.raise_for_failure()
```

废弃指令会保留在 manifest 中，但 `exec/batch/run/resume` 默认阻断。兼容、迁移、诊断或修复场景必须显式使用 `--allow-deprecated-command --deprecated-use-case migration`，Python API 侧对应 `allow_deprecated=True, deprecated_use_case="migration"`。

完整文档：`docs/USAGE.md`

## 目录

- `REQ_UeAgentInterfaceCMD.md`：需求说明
- `docs/USAGE.md`：使用说明
- `docs/ARCHITECTURE.md`：架构说明
- `docs/ROADMAP.md`：迭代路线
- `cli/uai_core/`：可复用执行核心与 Python API
- `cli/uai_cli/`：CLI 入口与旧模块导入兼容层
- `plans/`：计划模板
- `vars/`：变量模板
- `tmp/`：临时 JSON（自动清理）
- `reports/`：执行报告（自动清理）
- `logs/`：CLI 日志
- `tools/build.ps1`：打包脚本

## 许可证

本仓库使用 MIT License，见 `LICENSE`。
