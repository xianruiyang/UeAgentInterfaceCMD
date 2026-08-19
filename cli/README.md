# CLI 源码目录

`uai_cli` 正在重建为 `uai` SDK 的薄命令行外壳。公开 CLI 只允许处理 Connection
TOML、真实单指令参数和无损结果输出；不得直接访问 HTTP、加载本地业务
registry、拼装隐藏工作流或运行 release/coverage/quality gate。

旧 `command show/pack/route` 教程入口和旧组合 Gate 已删除。当前 CLI 只保留
无业务行为的包入口和版本输出；Client、Protocol、Connection TOML 与静态
command binding 完成后再补充正式调用面。
