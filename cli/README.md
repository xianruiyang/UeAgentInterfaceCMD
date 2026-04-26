# CLI 目录

主代码位于：`cli/uai_cli/`

- `main.py`：命令行入口与子命令分发
- `config.py`：配置与安全校验
- `http_client.py`：HTTP 调用封装
- `templating.py`：`plan + vars` 渲染
- `runner.py`：phase 执行引擎
- `niagara_guard.py`：Niagara 护栏
- `cleanup.py`：临时 JSON 自动清理
- `naming.py`：短命名生成
- `reporting.py`：执行报告
- `logging_setup.py`：日志初始化

