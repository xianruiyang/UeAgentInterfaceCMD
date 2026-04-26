# UeAgentInterfaceCMD 使用说明

## 1. 目标

`UeAgentInterfaceCMD` 是 `UeAgentInterface` 的外置命令行工具目录（主入口：`dist/uai-cli.exe`）。
它的作用是：

- 避免手写 HTTP
- 避免在命令行内联长 JSON
- 固化 `doctor / exec / batch / run / resume / namegen` 工作流
- 统一报告输出，便于失败定位与复盘

## 2. 前置条件

1. 打开 UE Editor 工程
2. 在 UE 中启动服务：
   - `Window -> UeAgentInterface -> Start UeAgentInterface Server`

## 3. 配置文件 `uai-cli.default.json`

默认配置文件位于：

- 开发态：`UeAgentInterfaceCMD/uai-cli.default.json`
- 打包版：`UeAgentInterfaceCMD/dist/uai-cli.default.json`（与 `uai-cli.exe` 同目录）

典型字段：

```json
{
  "base_url": "http://127.0.0.1:17777",
  "token": "",
  "timeout_seconds": 60,
  "clear_log_on_start": true,
  "log_level": "info",
  "niagara_guard_enabled": true,
  "niagara_guard_strict": true,
  "auto_cleanup_enabled": true,
  "cleanup_tmp_max": 120,
  "cleanup_tmp_keep": 40,
  "cleanup_reports_max": 200,
  "cleanup_reports_keep": 120
}
```

说明：

- `token` 可以留空：CLI 会尝试从项目 `Saved/Config/WindowsEditor/UeAgentInterface.ini` 读取（前提是你至少在 Editor 里启动过一次服务端以生成 token）。
- 默认只允许 loopback（`127.0.0.1/localhost`）；如确需非本机地址，使用 `--allow-nonloopback`。

## 4. 常用命令

下面示例均以打包版为主（推荐）。若使用开发态，把 `.\dist\uai-cli.exe` 替换为 `python .\run_uai_cli.py` 即可。

### 4.1 健康检查：`doctor`

```powershell
.\dist\uai-cli.exe doctor --json-output
```

建议：任何写操作前先跑 `doctor`，失败就停止排查，不要继续写。

### 4.2 单条命令：`exec`

```powershell
.\dist\uai-cli.exe exec --cmd list_actors --params "{}" --json-output
```

也可以把参数放到文件里（推荐，避免命令行转义）：

```powershell
.\dist\uai-cli.exe exec --cmd list_actors --params-file ".\tmp\list_actors.json" --json-output
```

### 4.3 一次性批处理：`batch`

```powershell
.\dist\uai-cli.exe batch --file ".\tmp\my_batch.json" --json-output
```

### 4.4 模板化执行：`run`（plan + vars）

```powershell
.\dist\uai-cli.exe run --plan ".\plans\sample_plan_list_actors.json" --vars ".\vars\sample_vars.json" --json-output
```

只展开模板不执行：

```powershell
.\dist\uai-cli.exe run --plan ".\plans\sample_plan_list_actors.json" --vars ".\vars\sample_vars.json" --dry-run
```

### 4.5 从报告恢复：`resume`

```powershell
.\dist\uai-cli.exe resume --report ".\dist\reports\task_*.json" --json-output
```

只从失败 phase 重试：

```powershell
.\dist\uai-cli.exe resume --report ".\dist\reports\task_*.json" --retry-failed-phase --json-output
```

### 4.6 生成短资产名：`namegen`

```powershell
.\dist\uai-cli.exe namegen --kind blueprint --base Door --tag-mode none --max-len 20 --json-output
```

## 5. `run` vs `batch` 怎么选

- 用 `run`：
  - 任务结构稳定、可复用
  - 希望把变量抽到 `vars.json`
  - 希望按 phase 分阶段执行（便于失败定位与恢复）
- 用 `batch`：
  - 一次性任务/临时验证
  - 步骤明确且不需要模板抽象

## 6. 输出位置（报告 / 日志 / 临时文件）

输出目录取决于运行方式：

- 打包版（`dist/uai-cli.exe`）：
  - 报告：`UeAgentInterfaceCMD/dist/reports/`
  - 日志：`UeAgentInterfaceCMD/dist/logs/`
  - 临时 JSON：`UeAgentInterfaceCMD/dist/tmp/`
- 开发态（`python run_uai_cli.py`）：
  - 报告：`UeAgentInterfaceCMD/reports/`
  - 日志：`UeAgentInterfaceCMD/logs/`
  - 临时 JSON：`UeAgentInterfaceCMD/tmp/`

报告里会带 `failed_index/failed_command/failed_error` 等字段；不要只看最后一条报错字符串。

## 7. 常见问题

### 7.1 `doctor` 失败

按顺序检查：

1. UE Editor 是否已打开项目
2. UE 菜单里是否已启动 `UeAgentInterface Server`
3. `base_url` 是否正确（默认 `http://127.0.0.1:17777`）
4. `token` 是否正确（或是否能从 `Saved/Config/WindowsEditor/UeAgentInterface.ini` 读取）

### 7.2 401 Unauthorized

说明 token 缺失或不匹配：

- 确认请求头/配置里的 `token`
- 在 UE 中使用 `Window -> UeAgentInterface -> Copy Connection Info` 获取当前会话的连接信息

