# UeAgentInterfaceCMD

`UeAgentInterfaceCMD` 承载 UAI 的公开 Python SDK、薄 CLI，以及只服务本仓库的
binding 和仓库诊断工具。它是模型连接远端 UAI 服务的客户端边界：Python 每次只
转发正式 manifest 中的一条真实指令，不实现第二套 UE 业务，也不在 Transport
Adapter 之外直接操作 HTTP。

## 公开入口

首次使用通过 `python.exe UeAgentInterfaceCMD/tools/sdk_environment.py install` 预装独立 SDK authoring 环境和用户级 `ueagentinterfacecmd` 命令。
日常直接调用 `ueagentinterfacecmd`；连续 SDK 脚本用同入口 `run -- <script.py>`，不用时 `uninstall` 一并卸载；路径以外层项目根为例。
具体安装、离线包源和卸载范围见 [安装与导入](docs/PYTHON_SDK_AND_CLI.md#安装与导入)。
从旧版升级时，以 [Pak 的升级说明](https://github.com/xianruiyang/UeAgentInterfacePak/blob/main/docs/UPGRADING.md)
选择匹配的 Plugin/CMD 版本，再运行本版本的 `sdk_environment.py install`。旧 `uai_core`、旧 exe 和连接模板
不作为当前 SDK 的兼容入口；独立 Connection TOML 仍是受支持的显式连接方式。

Python 调用只导入 `uai`，本地项目自动连接，独立连接也可使用 Connection TOML：

```python
import uai

with uai.connect_project() as client:
    result = client.execute("namespace.command", {"name": "value"})
```

CLI 与 SDK 共用 Client、Protocol 和 Transport，只提供连接检查与单指令转发：

```text
ueagentinterfacecmd connection show
ueagentinterfacecmd --connection connection.toml connection probe
ueagentinterfacecmd exec namespace.command --params-json "{}"
```

CLI 默认输出适合模型阅读的紧凑键值与 TSV；程序解析用 `--format json`，`--report` 始终保存完整 JSON。
Python SDK 仍返回原有结构化 Result。参数来源、精确 contract 调用、结果和退出码等正式用法见
[`docs/PYTHON_SDK_AND_CLI.md`](docs/PYTHON_SDK_AND_CLI.md)。指令身份和 schema
以 Plugin 的正式 manifest 为权威来源；`tools/uai_binding` 生成的静态 binding
只是可重建投影，不是第二份指令真源。

## 目录职责

- `cli/uai/`：唯一公开 Python SDK 包及其 client-only 内部分层；
- `cli/uai_cli/`：只依赖公开 `uai` 的薄命令行入口；
- `tools/uai_binding/`：消费正式 manifest 的确定性 binding generator；
- `tools/uai_repository/`：不进入 SDK import graph 的仓库诊断工具；
- `tests/`：保留在当前 Git 混合现场中的验证源码；
- `docs/`：当前 SDK/CLI 合同和维护说明；
- `templates/` 与 `build/README.md`：模板或受控构建输出说明，生成结果不作为
  源码、计划或状态真源；
- CLI report 只写入调用方通过 `--report` 明确选择的路径。仓库根不保留
  `logs/` 或 `reports/` 默认输出入口，项目运行证据按调用方的任务专属 `tmp/<run-id>/` 合同管理。
  既有 `runtimeLogs/` 只保留历史证据身份，不用于新输出。

## 生命周期与发布边界

- `retired/strict_v2/` 是按需精确读取的历史证据根，不属于普通实现发现面；
- 旧 `examples/`、`plans/`、`vars/` 与 `tools/dev-run.ps1` 已逐字节迁入
  `retired/strict_v2/legacy_cli_surface/`，只保留历史证据身份，不得导入或执行；
- `*.egg-info/` 是被忽略且可由打包工具重建的元数据，不进入版本控制；
- `docs/active/`、`tests/strict_v2/`、`tests/support/`，以及
  `tools/uai_repository/command_contract_generation/` 仍是受保护的 adoption residual。它们的
  权威拆分受 `DCR-UAI-TARGET-TAXONOMY` 与 `DCR-UAI-TARGET-PROVENANCE` 阻断，
  当前公开用法只由上文 SDK/CLI 入口定义；
- ignored cache、build、日志和运行输出可以重建，不得反推当前实现或任务状态；
- 本仓库的开发提交不等于 Pak/installed 发布；发布、同步和 gitlink 更新必须走
  各自正式流程。

仓库文本由 `.gitattributes` 统一为 LF。许可证见 [`LICENSE`](LICENSE)。
