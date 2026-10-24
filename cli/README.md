# Python SDK 与薄 CLI

`cli/uai/` 是唯一公开 Python SDK 包；`cli/uai_cli/` 是复用同一 Client、Protocol
与 Transport 的薄命令行外壳。两者都只转发正式 manifest 中的一条真实 UAI
指令，不加载本地业务 registry、不拼装隐藏工作流，也不在 Transport Adapter
之外直接访问 HTTP。

当前 console entry 为 `ueagentinterfacecmd`，`uai-cli` 保留为兼容别名。默认从当前目录向上定位最近的 UE 项目并托管连接；
也可显式传 `--project <目录或.uproject>` 或 `--connection <connection.toml>`。支持：

- `connection show`：读取并显示连接状态；
- `connection probe`：探测服务可达性；
- `exec <command_id>`：转发一条指令。

`exec` 的参数可从 `--params-json`、`--params-file` 或 `--params-stdin` 三者之一
提供，不传则使用空对象。stdout 默认使用 `compact`：缩进键值、行内标量列表和共享列名的 TSV 记录，
保留完整公开 Result 的字段和值。程序解析 stdout 时显式加 `--format json`；
`--report` 始终保存完整 JSON，与 stdout 格式独立。有附加公开诊断时，两种输出都包含顶层
`diagnostics`；SDK 通过 `Result.diagnostics` 读取完整数组，不受业务字段过滤影响。
`sdk_environment.py install` 同时安装 SDK 环境和用户级命令，无需激活即可使用：

```powershell
ueagentinterfacecmd exec query.command.search --params-json '{"intent":"clone"}'
```

`uninstall` 移除本次安装的用户命令和独立环境。Windows 使用原生 `.exe`，
避免 `.cmd` 包装器改变内联 JSON 引号。完整调用合同、返回值和退出码见
[`../docs/PYTHON_SDK_AND_CLI.md`](../docs/PYTHON_SDK_AND_CLI.md)。
