# strict_v2 历史证据

本目录只保存已经退出当前 SDK/CLI 职责面的 strict_v2 历史证据。这里的内容不属于
Python import graph，不定义公开 API、指令权威、当前任务状态或产品完成门禁，也不应
被执行、生成、回迁或用作新实现模板。需要调查历史决策时，应按已知路径精确读取。

## 内容与来源

- `generated_commands/` 保存 43 个旧的 command projection/helper 对象；分离前后
  Git tree 均为 `3261f4b75186b5950010e5fe9bec460a6754dc5f`。当前 binding owner 是
  `tools/uai_binding/`，正式指令身份与 schema 仍由 Plugin manifest 定义。
- `legacy_cli_surface/` 保存 23 个已经不适配当前 CLI 的旧示例、plan/vars 和开发入口。
  它们从原路径逐字节移动，来源指纹如下：

| 原路径 | 数量 | Git 对象 |
| --- | ---: | --- |
| `examples/` | 14 | tree `7840440619522b664f7bf07d2f0cc7843f900020` |
| `plans/` | 4 | tree `a088186aae46bd5ff80b1e3bb755a383cb6bcbd3` |
| `vars/` | 4 | tree `fb69e091d7f959311585309bfccba05e71520532` |
| `tools/dev-run.ps1` | 1 | blob `446c687f2648fa75a975ddbc6d9aabc57357dff8` |

其中 `plans/run_create_structure_20260304_173925.plan.json` 及其 vars 是一次真实的旧
UE 操作记录，因此保留为证据而不是删除。`tools/dev-run.ps1` 调用了当前解析器不再提供
的 `doctor`/`run` 表面，并且曾是这些 plan/vars 的唯一仓库内消费者；当前 CLI 只提供
`connection show`、`connection probe` 和 `exec`。

## 恢复与边界

分离前的直接父提交是 `cea042fb0c2689a8bab80151eb635d06d637bce9`。更早的恢复提交
`805e082bee60c8ed212b379f92f72608009e3602`（tracked baseline）和
`0b564958acf1d4a1ab10562ea03ae60b5ba0c4e2`（content baseline）继续保留原始证据。

外层未整理的 `readme.md` 和 Pak 固定的旧 CMD checkout 仍可能引用旧的
run/plan/vars 表面；它们是尚待独立裁决的发布侧引用，不是当前 CMD runtime owner，
也不能使本目录恢复为正式入口。当前公开用法只见仓库根 `README.md` 与
`docs/PYTHON_SDK_AND_CLI.md`。
