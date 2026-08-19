# Python SDK 与薄 CLI

`cli/uai/` 是唯一公开 Python SDK 包；`cli/uai_cli/` 是复用同一 Client、Protocol
与 Transport 的薄命令行外壳。两者都只转发正式 manifest 中的一条真实 UAI
指令，不加载本地业务 registry、不拼装隐藏工作流，也不在 Transport Adapter
之外直接访问 HTTP。

当前 console entry 为 `uai-cli`，支持：

- `--connection <connection.toml> connection show`：读取并显示连接状态；
- `--connection <connection.toml> connection probe`：探测服务可达性；
- `--connection <connection.toml> exec <command_id>`：转发一条指令。

`exec` 的参数可从 `--params-json`、`--params-file` 或 `--params-stdin` 三者之一
提供；`--contract-hash` 用于精确 contract identity，`--report` 可保存同一份无损
结果 JSON。完整调用合同、返回值和退出码见
[`../docs/PYTHON_SDK_AND_CLI.md`](../docs/PYTHON_SDK_AND_CLI.md)。
