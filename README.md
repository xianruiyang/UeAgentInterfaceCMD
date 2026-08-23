# UeAgentInterfaceCMD

`UeAgentInterfaceCMD` 承载 UAI 的公开 Python SDK、薄 CLI，以及只服务本仓库的
binding 和仓库诊断工具。它是模型连接远端 UAI 服务的客户端边界：Python 每次只
转发正式 manifest 中的一条真实指令，不实现第二套 UE 业务，也不在 Transport
Adapter 之外直接操作 HTTP。

## 公开入口

Python 调用只导入 `uai`，并从一份完整的 Connection TOML 建立 Client：

```python
import uai

with uai.connect("connection.toml") as client:
    result = client.execute("namespace.command", {"name": "value"})
```

CLI 与 SDK 共用 Client、Protocol 和 Transport，只提供连接检查与单指令转发：

```text
uai-cli --connection connection.toml connection show
uai-cli --connection connection.toml connection probe
uai-cli --connection connection.toml exec namespace.command --params-json "{}"
```

参数来源、精确 contract 调用、结果和退出码等正式用法见
[`docs/PYTHON_SDK_AND_CLI.md`](docs/PYTHON_SDK_AND_CLI.md)。指令身份和 schema
以 Plugin 的正式 manifest 为权威来源；`tools/uai_binding` 生成的静态 binding
只是可重建投影，不是第二份指令真源。

## 目录职责

- `cli/uai/`：唯一公开 Python SDK 包及其 client-only 内部分层；
- `cli/uai_cli/`：只依赖公开 `uai` 的薄命令行入口；
- `tools/uai_binding/`：消费正式 manifest 的确定性 binding generator；
- `tools/uai_repository/`：不进入 SDK import graph 的仓库诊断工具；
- `tools/tests/`：仓库工具自身的模块测试；
- `tests/`：SDK、协议、CLI 和边界行为的验证证据，不单独定义产品完成状态；
- `docs/`：当前 SDK/CLI 合同和维护说明；
- `templates/` 与 `build/README.md`：模板或受控构建输出说明，生成结果不作为
  源码、计划或状态真源；
- CLI report 只写入调用方通过 `--report` 明确选择的路径。仓库根不保留
  `logs/` 或 `reports/` 默认输出入口，项目运行证据按调用方的 scoped
  `runtimeLogs/<producer>/<task>/<run>/` 合同管理。

## 生命周期与发布边界

- `retired/strict_v2/` 是按需精确读取的历史证据根，不属于普通实现发现面；
- 旧 `examples/`、`plans/`、`vars/` 与 `tools/dev-run.ps1` 已逐字节迁入
  `retired/strict_v2/legacy_cli_surface/`，只保留历史证据身份，不得导入或执行；
- `*.egg-info/` 是被忽略且可由打包工具重建的元数据，不进入版本控制；
- `docs/active/`、`tests/strict_v2/`、`tests/support/`，以及
  `tools/uai_repository/command_contract_generation/` 和
  `tools/uai_repository/migration_evidence/` 仍是受保护的 adoption residual。它们的
  权威拆分受 `DCR-UAI-TARGET-TAXONOMY` 与 `DCR-UAI-TARGET-PROVENANCE` 阻断，
  当前既不作为公开用法，也不单独作为完成门禁；
- `historical_evidence` pytest marker 只标记仍绑定旧根计划任务收据的历史
  oracle。默认 pytest 选择明确排除这些 case；需要审计历史时可显式使用
  `python -m pytest -m historical_evidence`，其结果不得作为当前产品完成证据；
- ignored cache、build、日志和运行输出可以重建，不得反推当前实现或任务状态；
- 本仓库的开发提交不等于 Pak/installed 发布；发布、同步和 gitlink 更新必须走
  各自正式流程。

仓库文本由 `.gitattributes` 统一为 LF。许可证见 [`LICENSE`](LICENSE)。
