# UAI Generated Example Library

这些示例只覆盖外层 CLI 的标准调用形态。需要 UE 服务的示例默认是只读命令，适合 golden E2E smoke。

- `core_readonly.batch.json`: 世界状态和 actor 列表只读探针。
- `navigation_readonly.batch.json`: Navigation 只读摘要。
- `golden_readonly.plan.json`: 可用于 `uai-cli run --plan ...` 的 golden E2E 计划。
