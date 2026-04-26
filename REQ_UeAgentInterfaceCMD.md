# UeAgentInterfaceCMD 需求文档

## 1. 目标

构建一个面向 `UeAgentInterface` 的外置命令行工具，满足：

1. 用 JSON 模板批量执行，减少重复输入；
2. 遇错立即中断并返回中断位置；
3. 返回中断前已成功步骤结果；
4. 提供结构化报告，便于复盘；
5. 产出可独立运行的 `uai-cli.exe`。

## 2. 核心问题

直接手写 HTTP 调用存在：

- 参数重复且冗长；
- 步骤顺序脆弱；
- 出错后难恢复；
- 执行证据不集中（难排查）。

## 3. 功能范围（当前实现）

### 3.1 基础命令

- `doctor`：服务可用性检查
- `exec`：单命令执行
- `batch`：读取 JSON 批处理
- `run`：`plan + vars` 执行
- `resume`：失败恢复
- `namegen`：生成简短资产名

### 3.2 批处理执行语义

- 默认 `stop_on_error=true`
- 失败时返回：
  - `failed_index`
  - `failed_command`
  - `failed_request_id`
  - `failed_error`
- 返回 `results[]`（包含中断前成功步骤）

### 3.3 Niagara 稳定性护栏

- 自动 preflight（处理编辑器句柄状态）
- 自动 post-check（编译 + 编译日志 + emitter 列表）
- 拦截高风险操作：
  - 严格模式下禁止同一批次对同一 System 同时 remove/add emitter
- 发现 `Unknown Emitter`、编译错误、缺失 emitter id 即判失败

### 3.4 命名简化

- 统一短前缀（`BP/WBP/M/MI/NS/NE/LS`）
- 短标签模式（`none/time/date/datetime`）
- 默认短名，降低在 UE 内容浏览器中查找成本

### 3.5 自动清理

- 超阈值时自动清理 `tmp/*.json`、`reports/*.json`
- 保留最新 N 条，避免临时文件堆积

## 4. 非目标

- 不替代 UE 插件侧业务逻辑；
- 不扩展新的 UE HTTP 协议；
- 不做 GUI；
- 当前优先 Windows。

## 5. 交付物

- `dist/uai-cli.exe`
- `dist/uai-cli.default.json`
- `docs/USAGE.md`
- `docs/ARCHITECTURE.md`
- `reports/*.json`（运行时产物）

## 6. 验收标准

1. 能通过 `doctor` 正确识别服务状态；
2. `run/batch` 失败时可准确返回中断点；
3. 报告中可追溯成功步骤与耗时；
4. 护栏能在高风险 Niagara 批次中提前阻断；
5. `namegen` 能稳定生成简短可用资产名。

