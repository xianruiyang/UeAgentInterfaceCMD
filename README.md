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
- `templates/`、`reports/` 与 `build/README.md`：模板或受控输出落点说明，生成结果
  不作为源码、计划或状态真源。

## 生命周期与发布边界

- `retired/strict_v2/` 是按需精确读取的历史证据根，不属于普通实现发现面；
- `examples/`、`plans/`、`vars/`、已经 tracked 的 `*.egg-info`，以及 strict_v2
  相关 tests/docs 是受保护的 adoption residual；在消费者复核完成前不删除，也
  不作为当前 public usage 或完成门禁；
- ignored cache、build、日志和运行输出可以重建，不得反推当前实现或任务状态；
- 本仓库的开发提交不等于 Pak/installed 发布；发布、同步和 gitlink 更新必须走
  各自正式流程。

仓库文本由 `.gitattributes` 统一为 LF。许可证见 [`LICENSE`](LICENSE)。
