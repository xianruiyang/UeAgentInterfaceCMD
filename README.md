# UeAgentInterfaceCMD

`UeAgentInterfaceCMD` 是 `UeAgentInterface` 的外置命令行工具目录。  
目标是通过 `run/batch + JSON` 模板化执行，减少重复输入、提高稳定性和可追踪性。

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

