# build 目录说明

本目录用于说明打包相关信息，不存放实际运行时产物。

实际打包产物输出到：

- `dist/ueagentinterfacecmd.exe`

默认发现当前 UE 项目，也可用 `--project <目录或.uproject>` 或 `--connection <connection.toml>` 显式选择。
连接共用公开 SDK 实现，不随可执行文件附带第二套默认配置。
