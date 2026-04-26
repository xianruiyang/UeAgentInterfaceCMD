# UeAgentInterfaceCMD 架构说明

## 1. 模块划分

- `uai_cli.main`
  - 命令行入口与参数解析
  - 子命令分发：`doctor/exec/batch/run/resume/namegen`
- `uai_cli.config`
  - 配置加载、覆盖与校验
  - loopback 安全限制
  - Niagara 护栏与自动清理配置
- `uai_cli.http_client`
  - HTTP GET/POST 封装与错误转换
- `uai_cli.templating`
  - `defaults + vars` 合并
  - `{{var}}` 模板渲染
  - phase 结构归一化
- `uai_cli.runner`
  - `exec_batch` 执行引擎
  - phase 顺序执行与失败中断
- `uai_cli.niagara_guard`
  - Niagara 变更护栏（预处理 + 结果校验）
- `uai_cli.cleanup`
  - `tmp/reports` JSON 自动裁剪
- `uai_cli.naming`
  - 简短资产名生成（前缀 + 可选短标签）
- `uai_cli.reporting`
  - 执行报告生成与落盘
- `uai_cli.logging_setup`
  - CLI 日志初始化（含 hostname）

## 2. 执行链

1. 入口解析参数与配置（支持命令行覆盖默认配置）。
2. 按需执行自动清理（启动阶段）。
3. 执行子命令：
   - `doctor`：`/api/ping` + `/api/status`
   - `exec`：单次 `/api/exec`
   - `batch`：读取 JSON 后走统一 `execute_batch()`
   - `run`：读取 `plan + vars`，按 phase 调 `execute_batch()`
   - `resume`：从报告失败点继续
   - `namegen`：生成短资产名
4. 记录报告与日志。
5. 命令结束后再次执行自动清理。

## 3. Niagara 护栏机制

### 3.1 预处理

当批次包含 Niagara 变更指令时：

- 自动注入 preflight：关闭资产编辑器句柄（避免 stale editor state）。
- 严格模式下，拦截“同一 system 同批次 remove_emitter + add_emitter”。

### 3.2 后校验

对每个触及的 NiagaraSystem 自动注入：

- `niagara_compile_system`
- `niagara_get_compile_log`
- `niagara_system_list_emitters`

若出现以下任一情况，批次判失败：

- 编译日志含错误；
- emitter 列表出现 `Unknown Emitter` / `Unknown Em`；
- emitter 缺失 `id`。

## 4. 命名策略

- 统一前缀：`BP/WBP/M/MI/NS/NE/LS`
- 支持 `tag_mode`：`none/time/date/datetime`
- 默认输出短名，降低在 UE 内容浏览器中的检索成本

## 5. 报告模型

每次执行输出结构化报告，包含：

- 任务 ID、时间戳、配置快照（token 脱敏）
- phase 级执行结果
- 失败索引与失败指令
- 耗时分解：`t_prepare_ms/t_http_ms/t_parse_ms/t_verify_ms/t_total_ms`

## 6. 安全与约束

- 默认仅允许 loopback（`127.0.0.1/localhost`）
- token 必须来自配置或参数，不写死在代码里
- 报告中 token 脱敏

