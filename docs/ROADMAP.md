# UeAgentInterfaceCMD 路线图

## P0（已实现）

- `doctor / exec / batch / run / resume` 子命令
- `plan + vars` 模板渲染
- phase 级 `exec_batch` 执行与失败中断
- 结构化报告输出（含失败点与耗时）
- 日志文件输出（主机名后缀 + 版本标签）

## P1（待做）

- 失败自动分类（参数错误/连线错误/编译错误）
- `resume` 更细粒度恢复（按步骤恢复）
- 常用场景模板库完善（蓝图、UMG、材质、Niagara、关卡）

## P2（待做）

- 报告差异对比（两次执行）
- 一键诊断包（CLI + UE log 汇总）
- 可视化执行摘要（可选）
