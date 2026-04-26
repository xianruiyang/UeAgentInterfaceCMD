# UeAgentInterfaceCMD

`UeAgentInterfaceCMD` 是 `UeAgentInterface` 的外置命令行工具目录。
目标是通过 `run/batch + JSON` 模板化执行，减少重复输入、提高稳定性和可追踪性。

它与 `UeAgentInterface` 插件仓库配套使用：插件运行在 UE Editor 内，CLI 在外部发起 doctor、run、batch、报告读取和清理等流程。

## 代码来源说明

本仓库的初步代码是使用 GPT 编写，并在实际 Unreal Engine 自动化工作流中持续调试、测试和修复。后续维护应以 CLI 单测、UAI 报告、UE 编译/运行验证和文档同步为准。

## 当前重点

- 统一入口：`dist/uai-cli.exe`
- 推荐模式：`run`（plan + vars）与 `batch`（JSON 文件）
- 命名简化：内置 `namegen`，默认生成短资产名
- Niagara 护栏：自动 preflight + 编译/日志/emitter 校验
- 自动清理：`tmp/reports` 超阈值自动裁剪

## 快速开始

```powershell
.\dist\uai-cli.exe doctor --json-output
.\dist\uai-cli.exe run --plan ".\plans\sample_plan_list_actors.json" --vars ".\vars\sample_vars.json" --json-output
```

完整文档：`docs/USAGE.md`

## 目录

- `REQ_UeAgentInterfaceCMD.md`：需求说明
- `docs/USAGE.md`：使用说明
- `docs/ARCHITECTURE.md`：架构说明
- `docs/ROADMAP.md`：迭代路线
- `cli/uai_cli/`：CLI 主代码
- `plans/`：计划模板
- `vars/`：变量模板
- `tmp/`：临时 JSON（自动清理）
- `reports/`：执行报告（自动清理）
- `logs/`：CLI 日志
- `tools/build.ps1`：打包脚本

## 许可证

本仓库使用 MIT License，见 `LICENSE`。
