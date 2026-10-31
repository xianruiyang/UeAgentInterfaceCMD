# Python SDK 与 CLI

`UeAgentInterfaceCMD` 对调用方只暴露远程调用能力。Python 不实现 UE 业务、
HJSON、Planning、State、Verification 或领域规则；这些语义由 C++ UAI 服务端
唯一拥有。

结果中的 `warnings` 保留服务端观察诊断，普通结果、operation 结果及声明式精简结果均透传。
一致性警告不改变 `ok`，也不触发 `raise_for_error()`；输入错误和真实执行失败仍使用错误合同。
SDK/CLI 不把警告解释成重试、回滚或改写资产的指令。

当前版本只提供 HTTP Transport Adapter，但 Client、Protocol、静态 command
method 和 CLI 不依赖 HTTP 类型。以后增加 TCP、UDP 或其他 Transport 时，公开
command 调用方式不变。

## 安装与导入

在 CMD 源码目录外或项目根目录执行一次显式安装：

```text
python.exe UeAgentInterfaceCMD/tools/sdk_environment.py install
python.exe UeAgentInterfaceCMD/tools/sdk_environment.py status
```

该入口在 CMD 的 `.venv-sdk` 创建专用 Python 环境，editable 安装当前 SDK 和
`authoring` 可选依赖（HJSON 文件解析库）。依赖声明唯一维护在 `pyproject.toml`；
HJSON 的资产语义仍由服务端拥有，解析库仅用于编辑导出的文本。不会改变全局 Python。
同次安装把原生 `ueagentinterfacecmd` 入口放到用户 `~/.local/bin`，指向该独立环境；Windows 文件名带 `.exe`。
Windows 缺少该目录时补充用户 PATH，已有终端或宿主需重新打开以继承；其他系统按安装提示配置 shell PATH。
安装记录只用于识别本工具拥有的入口，不覆盖其他软件的同名文件。`status` 同时报告入口归属和 PATH 实际命中。
首次安装需要可用包源；已准备 wheel 时可用 `install --no-index --find-links <wheel目录>`。
安装继承调用进程的 pip/代理配置，不自动绕过代理或关闭 TLS 校验。环境变量使用 SOCKS 代理时，
安装器经调用方 Python 的可用代理支持下载 PySocks wheel，再离线安装到专用环境；也可由 `--find-links` 提供该 wheel。
调用方也缺少代理支持时明确保留安装错误；已安装环境的日常运行不需要包源。
更新前暂存本工具自有环境和 CLI；依赖安装、导入校验或入口发布报错时恢复先前状态，首次失败移除半成品。
恢复遇到锁定文件等错误时，明确给出保留的备份目录，不删除尚需恢复的原安装。用户共享 PATH 项继续保留。

日常执行复用环境，不重新安装、不访问包源：

```text
ueagentinterfacecmd exec query.command.search --params-json '{"intent":"clone"}'
python.exe UeAgentInterfaceCMD/tools/sdk_environment.py run -- tmp/my-task/create.py
```

也可直接调用 `.venv-sdk/Scripts/python.exe`（Windows）或 `.venv-sdk/bin/python`。
`cli` 转交已安装的 CLI，`run` 原样传递 Python 参数；两者保留工作目录与退出码。
公开 `uai.connect_project()`、CLI 和项目 `project_uai_client()` 共用 CMD 的项目连接实现。
该环境的 editable 安装指向当前源码，所以普通 SDK 源码更新无需每轮重新安装。依赖声明变化时显式重跑 install。
环境缺失或安装失败时明确报错，不在普通调用中静默 pip 安装。

不用时通过基础 Python 卸载，移除本次安装的用户 CLI 入口、安装记录和自有 `.venv-sdk`：

```text
python.exe UeAgentInterfaceCMD/tools/sdk_environment.py uninstall
```

卸载保留共用的用户 bin 目录与 PATH 项、其他安装接管或外部替换的同名入口，不删除源码、UE 内容、任务脚本或用户其他环境；不关闭 UE。已有自行管理的 Python
环境也可按标准 `pip install -e "./UeAgentInterfaceCMD[authoring]"` 安装，生命周期由调用方管理。

业务代码只导入一个包：

```python
import uai
```

`import uai` 不读取配置、不连接网络、不启动线程，也不触碰 Unreal Editor。

本地项目无需手工准备连接文件或凭据：

```python
with uai.connect_project() as client:
    result = client.editor.dirty_resources()
    result.raise_for_error()
```

省略项目时从当前目录向上查找最近的 `.uproject`；也可传项目目录或 `.uproject` 文件路径。
显式指定目录时只使用该目录；同一目录存在多个项目时须指定文件。可选 `io_timeout_seconds` 控制调用超时。
连接复用项目 UAI 配置，临时连接文件不含凭据且离开上下文时清理。独立连接继续使用下述 `uai.connect()`。

## 独立部署的 Connection TOML

显式连接独立部署时使用 `uai.connect("connection.toml")` 或 CLI `--connection`；
本地项目沿用上面的托管入口，不搜索或复用其他任务的连接文件。
一份 TOML 包含一次连接所需的全部网络配置。当前 C++ public command ingress
使用 `/api/uai/command`：

```toml
format_version = 1

[connection]
transport = "http"
endpoint = "http://127.0.0.1:17777"

[protocol]
version = "current"

[timeouts]
connect_seconds = 5.0
io_seconds = 120.0

[authentication]
mode = "bearer_env"
bearer_env = "UAI_AUTH_TOKEN"

[transport_options.http]
tls_verify = true
route_path = "/api/uai/command"
probe_path = "/api/ping"
auth_header = "X-UeAgentInterface-Token"
```

连接文件采用严格字段校验。当前 command ingress 强制认证，正式模板通过
`UAI_AUTH_TOKEN` 环境变量显式引用 secret；TOML、业务调用、command params、日志和
manifest 都不保存 token。也可以使用 `bearer_file` 引用只含 token 的受控文件。
`connection probe` 只证明与 command route 同属一个 owned transport 生命周期的
ping route 可达；probe 不进入 CommandService，也不证明 command 认证。只有真实
command Result 才证明认证后的 public command edge 可用。

并发 command 由服务端公共入口接收并排队，在 GameThread 上顺序执行；一个较慢的
command 不阻塞网络接入或 ping。等待队列已满时返回 `transport_backpressured`，
并明确说明该请求尚未执行。SDK 保留具体原因，不自动重试或重放。入口发现客户端断开时，
仍在排队的请求会跳过；已经开始执行的请求可能继续完成，断连本身不能证明操作失败。

## SDK 调用

本地项目使用托管连接，命名方法只发送一条对应的真实 command：

```python
import uai

with uai.connect_project() as ue:
    result = ue.query.command_search("editor runtime inspect")

if not result.ok:
    print(result.error)
else:
    print(result.payload)
```

当前由 C++ 正式 manifest 生成的命名方法包括：

```python
ue.query.command_search(intent)

ue.query.command_usage(commands)

# 复杂合同由生成 SDK 方法提供

ue.editor.open_assets()

ue.asset.factory_candidates(
    "asset.object.create",
    query="file media",
)

ue.reference.origin_resolve(
    input={"target": {"source": "ue_object", "asset_path": object_path}},
)

ue.project.summary()

ue.query.content_search(
    content_kinds=["actor", "component"],
    terms=["door"],
)

ue.content_graph.compound(
    target,
    input={
        "sections": [
            "summary",
            "structure",
            "items",
            "relations",
            "properties",
            "parameters",
            "diagnostics",
        ],
        "include_closure": True,
    },
    context={...},
    projection={...},
)

workspace = ue.content_graph.export_workspace(
    target,
    name="current",
    profile_id="llm_authoring",
)

workspace.result.raise_for_error()
print(workspace.path)
```

随后通过文件工具直接编辑导出的普通 HJSON。增删属性、节点、连接和结构项不需要
Python 解析/重写脚本；大量重复生成或计算变换才按需脚本化。文件编辑结束后，新的
Client/Python 进程可以继续导入，不必重新导出或维持原对象存活：

```python
workspace = ue.content_graph.open_workspace(target, name="current")
result = workspace.import_changes()
result.raise_for_error()
```

`open_workspace` 只用同一项目、target 与短 name 恢复目录句柄，不连接服务端、不读隐藏清单、
不导出或写入目录，因此不会覆盖尚未应用的文件编辑。它的 `workspace.result` 是 `None`，
不伪造导出成功；目录是否存在、目标是否匹配、基线是否有效由原服务端导入链判定。

导入由 SDK 内部推进既有 operation，正常仍返回最终业务 `Result`。传输超时不表示导入未执行；
取得接受响应中的 operation 后，SDK 保留本次操作 custody，后续超时结果的 `error.recovery_action` 给出 `resume_import:<名称>`。
使用 `ue.content_graph.resume_import("该名称")` 取得同一导入的最终结果，不重新调用 import 重放修改。
恢复限于同一 Editor 会话；Editor 重启后先核对实际状态，不将未知结果当成未应用。
首次接受响应本身未取得时没有可用恢复 handle，同样先核对实际状态，不能直接重放。

当前公开命令集合以 C++ 冻结 `FUeAgentImmutableCommandRegistry` 的正式 manifest
为唯一依据，覆盖 Query discovery、Read/Export、Reference CRUD、
SimpleAuthoring、Timeline/Spatial、GraphCompound、Destructive/Import 与
LongRunning/Session 等模块。命名方法全部由该 manifest 生成，Python 不手写或
补充第二份命令列表；硬编码命令数量既不是同步机制，也不代表每条 command 都已
获得完整 E3/E4 真实 UE 证据。

创建资产时，优先以 `create_command="asset.object.create"` 调用
`asset.factory.candidates`，只使用返回的可读名称，必要时附带必要的短语义 `select`，
再交给生成 SDK 创建方法。服务端 factory reference 和 catalog revision
只由服务端内部拥有，不是模型输入。factory catalog、官方插件可用性和不支持语义只由服务端拥有；
SDK 不扫描源码、猜 class path、弹出交互配置窗口或在插件缺失时伪造成功。

`content_graph.compound` 的领域合同要求 `input.sections`。SDK 不在客户端
补业务默认值；完整 authoring Export 需要的 sections 和 closure 默认由
服务端 `content_graph.export_workspace` command 统一拥有。

导出 HJSON 本身只承载可编辑字段、enum 和必要元数据；机器身份与并发基线留在服务端隐藏
manifest 中。缺失结构项时通过
command search/usage 找到生成 SDK 方法，并使用节点、Actor、Component 或 Module 查询补齐可读候选。导出不足且搜索也无法覆盖时报告能力缺口，不回退到 Python 业务实现。

Item 可带只读的 `unit.definition` 可读引用，指向共享 `definitions.hjson` 中的值类型定义及其字段定义。
编辑业务值时保留此引用；它不属于 `unit.values`，不能用修改定义引用来改变实例身份或类型。
只在实际导出带有该字段时读取，不为其他 Item 自行补造定义。

普通属性行同样区分 `type`、`value` 和可选只读 `definition`：`type` 是稳定值类型，基础类型不加定义序号；enum/struct 保留完整原生路径，bitmask/PCG selector 还保留其专用类型标识。约束、候选和元素模板按 `definition` 在所属 `definitions.hjson` 中读取，不能用 `type` 查完整属性定义。定义引用只在当前导出目录有效，编辑值时保留它。

模型通过 `content_graph.export_workspace(target, name=...)` 得到
`HjsonWorkspaceHandle`，或通过 `open_workspace(target, name=...)` 打开已导出的目录，
再用 `workspace.import_changes()` 导入；绝对路径只由 SDK 和
wire 私下持有。目标类型、解析、Planning、执行、验证、保存和读回事务全部由 C++
服务端负责。领域 mutation
意图写在对应 HJSON schema 中，不存在旧 `intent` 或 `dry_run` 公开参数。
普通编辑必须使用 Export 产生的同一工作区根目录；目录编辑所需的
target、workspace manifest 和并发基线由服务端从隐藏 manifest 恢复，调用方不读取或回填。
普通编辑只修改模型可见 HJSON；不得修改
`.uai/workspace.hjson` 的 machine inventory、identity、revision、content/edit hash 或
fingerprint，服务端 Import 会依据该不可变基线重算已编辑 unit 的当前 hash 与语义指纹。
`workspace.import_changes()` 也不解析或刷新这份隐藏基线；多个 unit 可以按不同 pointer 共用同一
普通文件，unit 的语义摘要不能替换为整个文件的摘要。文件与指针合法性继续由服务端导入入口校验。
HJSON 失败的公开定位位于 `result.error["diagnostic"]`：`diagnostics` 汇总多个可靠错误，
`source_file/line/column/json_pointer` 定位输入；`unchecked` 指出因语法、结构或依赖失败而未检查的范围，
嵌套 `cause/diagnostics` 也可携带各自的 `unchecked`。公开诊断不再输出由空列表推导的 `complete`；
未列未检查项不表示已检查全部输入。单错误可以直接使用顶层诊断。`raise_for_error()` 同样展示这些
已经公开投影的字段，不再仅显示通用失败文字；SDK 不自行解析 HJSON，也不改变错误输入后重试。
SDK 的 `Error.diagnostic` 同样保存结构化公开事实，CLI 和项目 runner 整体传递。协议拒绝同样携带
`error.diagnostic`，SDK 的 `ProtocolError.diagnostic` 原样保留该对象及嵌套原因，不再从 message-only
的旧协议错误重建诊断。普通业务值中的 `identity/hash` 等键不作为过滤依据。本地路径、配置、
参数错误在产生点写明字段、必要值与已有文件位置。PIE 启动、持久绑定检查和操作恢复失败保留
已有服务端诊断，仅补恢复状态，不把失败重新变成笼统的本地提示，不从 `str(error)` 反解析原因。
配置读取错误不会回显认证内容；continuation 错误只公开字段名和状态，不公开机器身份或 revision。
未绑定文件的输入错误以 `semantic_pointer` 定位语义字段；仅有该字段时不代表已知文件或行列。
原始位置和原因在领域交接、回滚事实补充后继续保留，不需要调用方解析私有错误文本。
复杂值比较由源头递归产生具体字段/元素路径及必要的 `expected_value/actual_value`，后续仅补来源与上下文；
公共摘要不会把差异值替换成相同的字段数量。`*_value_present: false` 表示缺失，和显式 null 不同。
工作区冲突在同一路径保留 `proposed_value`；编辑发生在不同路径时，保留独立的结构化编辑差异。
导入准备阶段的属性类型断言也在产生处绑定原 workspace 来源；类型定义仅存在于隐藏元数据时，
返回所关联公开属性的文件与位置并标 `related_input`，不将该位置冒充错误类型字段。领域返回的语义指针
由公共 document source binding 解析回原文件，不要求 SDK 读取或重建来源映射。
首次导入和 single_file 同样保留原始 AST 来源，内部转换出的 World/HLOD 文档使用来源映射返回原文件。
已知字段定位到原字段；缺失字段或原生错误仅能关联父级时明确标为 `related_input`，不使用内部重排后的行号。
外部输入的 factory、skin-weight、localization 也属于 `import_workspace`：原始来源贯穿准备、参数校验和
委托执行，参数错误映射回 source/options/target_policy 字段；最终 lifecycle 诊断包含回滚追加原因。
公共操作的持久验证失败使用同一 `error.diagnostic`：已声明的 `verification` 整体保留，
其中 `targets[].comparison.differences` 保留比较器的 `kind/path/left/right`，`targets[].target` 给出业务
类型、角色与结构化 selectors；path 中的 entry 使用本次比较的短索引，如
`/entries/0/value/triangle_count`，不暴露复合内部身份。类型化 identity/revision 证据去除机器信息，
普通业务属性同名字段仍保留。验证状态、结果及嵌套事实不由诊断出口重新挑选。oracle 无法读取时，
`cause` 给出实际 oracle 阶段、原因码及结构化下层诊断。普通指令/原生失败原因由服务端公共出口
传递源头显式构造的 `diagnostic.message`；嵌套原因使用自身错误码，位置、子诊断、未检查范围、修正建议和
预期/实际值逐层保留。显式私有上下文和机器身份不公开；SDK 不自行从未知私有文本猜测诊断。
这些字段同时适用于 SDK 与 CLI；`state_unknown` 或 `retry_safe=false` 时不能据失败自动重放写入。
候选查询保留源头目录覆盖与支持缺口，不能用匹配数等于返回数代替完整覆盖。已知缺口返回结构化失败；
SoundCue、MetaSound、UMG 的已声明部分目录能力继续可用，成功 payload 的 `diagnostics` warning 说明范围。
创建候选返回原名并保留内部独立身份，实际歧义返回短 `choose` 字段供 `select` 重试，不从拼接名称重建身份。
同名不同模块、目录、函数库或原生配置保留可读区别；来源 breadcrumb 由服务端投影，只在必要时作为
一项或两项选择字段返回。模型原样回填 `choose`，无需填写 class/asset 路径、机器身份或菜单序号。
MetaSound 创建选择与原生 Builder 一致：同 class 的主版本选择其当前最高次版本，旧次版本不列为独立可创建选项。
已有有效静态或动画 SparseVolumeTexture 可用同一 workspace 流程编辑设置：在实际导出的
`properties.hjson` 中修改 `AddressX/Y/Z` 的原生 `TextureAddress` 值，以及
`StreamingPoolSizeFactor`、`NumberOfPrefetchFrames` 等流送字段，再 import 并独立 export 读回。
保留导出的 type/value 形状与其他字段；材质通知、帧缓存重建、流送刷新和保存重载由服务端与 UE 原生逻辑承担。
内部 Frame 不作为独立资产创建或编辑，体素来源仍由原生 importer 负责；此设置流程不提供空 SVT factory 或 VDB 转换器。

已有 SubUVAnimation 也使用该 workspace 流程：`SubUVTexture` 以导出的资产路径或 `null` 表达，
`SubImages_Horizontal/Vertical`、`BoundingMode`、`OpacitySourceMode`、`AlphaThreshold` 沿用导出的原生字段和值。
只编辑需要变更的行；清空源纹理不会隐式重置其余属性。UE 原生通知重建派生包围几何，源纹理内容保持为引用输入，
SDK不重写像素或实现几何生成。导入后重新 export 核对引用和设置；此编辑流程不承诺空资产 factory 创建。

TextureCollection 可由公开 factory 候选 `Texture Collection` 创建，再通过普通 workspace 编辑 `Textures`。
保留导出的 `object_ref[]` 形状，value 数组使用纹理资产路径或 `null`；顺序、重复项、移除和空数组均可表达。
导入后独立 export 核对；错误类型引用会被拒绝。资源集合和引用材质更新由 UE 原生逻辑承担，SDK 不改纹理像素或启用 bindless。

Texture2DArray 的公开创建候选名为 `Texture 2DArray`，须消费实时查询返回的名字。
普通 workspace 的 `SourceTextures` 使用有序纹理路径数组；重复项合法，空数组清除生成内容，null或无源数据纹理会拒绝。
UE负责尺寸、格式与gamma转换。源列表与格式设置一起变更时，先生成源再应用本次明确修改的格式字段；
未修改的设置可能随原生来源通知重新推导，导入后独立 export 核对最终值。此流程不替代外部DDS importer。

TextureCubeArray 的公开创建候选为 `Texture Cube Array`，同样编辑普通 `SourceTextures` 有序数组。
每个引用代表一个Cube；可使用一致的六面来源或单图long-lat来源，尺寸/格式/面数不匹配会拒绝，不自动转换成兼容来源。
空数组清除生成Source和资源。它与Texture2DArray共用属性解码、源优先的分阶段应用和事务；Cube面生成仍由UE负责。

TextureCube 可由实时候选查询返回的 `Texture Cube` 创建。导出普通 workspace 后，编辑 `source_input`
的 `value` 对象：按 `positive_x`、`negative_x`、`positive_y`、`negative_y`、`positive_z`、`negative_z`
填写六张现有 Texture2D 的资产路径。六张来源须有有效、单切片、正方形且尺寸/格式一致的源数据。
PNG 来源可先通过 [Factory 导入](active/t28_external_factory_import.md) 创建；SDK 不拼装像素。
本次明确编辑的纹理设置与六面生成一起提交。导入后独立 export 核对最终设置；六个引用是一次性输入，
重新导出会返回空模板，不表示保存了引用数组。整份空模板不发起生成，部分填写或 null 面会被拒绝。
生成内容的保存重载和失败恢复由公共事务承担，来源资产不修改；内部 Source 摘要不会出现在可编辑 HJSON 中。

VolumeTexture 的公开候选为 `Volume Texture`，同样消费实时查询返回的名字创建。
普通 workspace 的 `source_input.value` 使用对象内的 `slices` 有序资产路径数组，
按数组顺序生成深度切片。接受1–512张尺寸/格式一致、具有有效单切片源数据的Texture2D，允许非正方形切片。
空数组表示未提交生成输入；null或不兼容来源拒绝。成功后原生逻辑清除旧Source2DTexture/TileSize，
重新export返回空输入模板；切片引用不是持久数组。公共事务覆盖生成Source和旧来源元数据的保存重载及失败恢复。

当前 Sequence 普通目录按导出的 categories、root_tracks/tracks 及嵌套 sections/channels/keys 编辑；
既有 Float 轨道支持改显示名、删除与清空，未知新轨道写前拒绝。
track/section的properties按类别使用公共type/value与递归稀疏编辑，object_property_definitions提供集中定义。
DisplayName只由display_name编辑，SectionRange只由range编辑；原生section模板同时提供属性默认。
String/Bool/Integer/Byte/Float/Double/Color/Vector/受支持Transform 的 scalar channel 与 key 复用公共集合，Double 保留原生精度；
String的value_lexeme保留完整文本，空字符串default与未设置不同，不提供虚构tangent/外推属性。
ObjectPath以value的path/null及value_definition表达引用，不与value_lexeme混用；null key合法，null default等于unset。
track_kind保留导出的原生类名，不作为创建选择器；Vector新section模板继承实际维数。
Bool值只接受true/false词法，不接受数字强转或伪造key切线字段。
Integer使用严格int32词法/范围，channel.properties支持原生插值开关。
Byte无Enum时为0..255；有Enum时从value_lexeme_definition选择原生名，新key遵守显式选择要求。
新增section直接使用section_definitions中所属轨道引用的原生通道模板。
key.properties通过公共Struct codec编辑插值/切线，省略字段保持；value_lexeme仍唯一持有key值。
key_definitions按轨道和channel引用含原生默认与属性/枚举定义的模板。
channel_definitions说明channel.default的is_set有值/无值分支及channel.properties前后外推。
具体已验证范围见
[Sequence workspace contract](active/t22_sequence_domain.md)，不由原生完整 structure replacement
或初始化合同反推普通目录支持范围。Localization target 使用
显式 create/update/upsert/remove。字段省略、preserve、remove/null/default 的适用性只由
对应服务端 schema 决定。并发、授权和验证信息由服务端从隐藏 workspace manifest 与内部验证上下文恢复。

领域 candidate 返回值不是由 Python 翻译的通用 seed。普通 Export→编辑→directory Import
的模型可见 semantic workspace 中，新 keyed item 直接写最小可读 `name: ...`；map key
使用 owner 作用域内的短可读 alias，精确实例身份由隐藏映射持有。服务端公共 projection
只在内部构造 hidden candidate。不得在这类 structure HJSON
中写旧的嵌套 candidate envelope。只有领域教程明确给出的完整 legacy/domain document 才服从
其自身 legacy candidate envelope。候选 selector 只允许 `name` 与必要的短语义 `select`；明确知道且当前导出声明的 `class_path`、`asset_path`、
factory 等字段可以作为 assertion，但不要求复制完整搜索行。Blueprint node 候选公开的
function/event/variable/node 语义字段也只能在当前导出、生成 SDK 或正式 schema 明确暴露时作为 assertion；不得从
显示名合成，且内部 `native_action_signature` 不公开。graph/pin、SCS parent、World/level、stage、
placement 和稳定实例身份属于结构上下文，不得混入选择器。
服务端在首写前从同一 UE 原生 owner 重枚举并唯一解析选择器，再调用同一
action/spawner/factory。SDK 不重建 node class、Component class、asset factory 或 asset
mapping；candidate query 不返回 revision；Import 的并发基线也由服务端隐藏工作区证据持有。
当前稳定入口包括 `blueprint.node.candidates`、
`blueprint.component.candidates` 和 `world.actor.candidates`；具体参数以生成 SDK 签名为准。

三种 carrier 在 C++ source loader 中先收敛为同一个只读 resolved source。服务端在隐藏
证据面维护来源完整性、语义等价性和目录基线，因此仅改变 inline、single-file、directory
或空白/字段顺序不会改变业务计划。以上证据均为服务端内部合同，调用方不读取、构造或传入。

成功的 `content_graph.export_workspace` 返回最小公共状态 `{"status":"succeeded"}`。
已发布后的清理异常额外返回 `warnings`，不改变成功状态；无需因此重复导出或导入。
语义目录 `import_workspace` 成功后额外返回 `workspace_refresh: {status: "refreshed"}`：服务端已经沿
原 exporter 将输入目录整理为标准结构和新基线，保留无关用户文件；可继续编辑同一 workspace，
不必手工清理临时创建表达或再次 export。非目录输入与旧版结果没有该刷新承诺。
生成分片的归属由 publisher 收据维护；替换图时省略旧引用不使原生成文件变成用户文件。
用户额外文件在后续连续刷新中仍保留。旧收据无法区分来源时，仅合并同路径且字节相同的内容；
不同内容的冲突不会静默覆盖，按下述已应用后失败边界恢复。
`workspace_refresh.warnings` 仅描述成功发布后的清理问题，不应因此重复 import；
它与下述旧 durable 事务恢复警告具有不同的来源和处理含义。
服务端仍必须在返回成功前完成该领域所需的
apply、compile/settle、save/reload 和内部独立读回；这些执行证据不作为默认
模型结果重复回显。需要确认实际持久状态时，调用方应使用正式 Query 或重新
Export；失败仍返回稳定的 typed failure，SDK 不补真值或把部分结果升级为成功。

成功的语义目录导入另返回 `execution_timing`（`scope: "server_directory_import"`）：
`source_prepare_seconds`、`domain_import_seconds`、`workspace_export_seconds`、
`workspace_refresh_other_seconds`、`total_seconds`。这些秒数由现有服务端入口计时；
domain_import 包含内部规划、应用、更新、保存和读回，尚不拆分这些内部阶段；refresh_other
包含刷新目录准备、发布和清理。它们不包含客户端等待/网络或模型时间，不改变成功与恢复语义。
非目录输入和旧版本结果没有这些字段，不将缺字段解释成零耗时；调用方可另记录本次调用墙钟时间。

`content_graph_import_applied_workspace_refresh_failed` 表示资产已经应用，但目录刷新未完成。
`Result.error["diagnostic"]` 保留 `asset_applied: true`、`retry_import: false`、
`retry_safe: false`、`transaction_status: "committed"`、底层 `cause_code` 和
`recovery_action: "export_current_asset_to_new_workspace"`。不要重放 import；处理原因并重新
export 到新目录后继续。已应用后的结果编码失败也使用同一恢复边界，不伪装为未发生写入。

导出发布或 `workspace_refresh` 成功后，若发布日志更新、备份或临时目录清理失败，
`warnings` 数组返回公开诊断对象，包含 `code`、`severity: "warning"`、`message` 及必要的目标、
位置和原始原因。调用方完整保留对象，不再只提取错误码；这些警告不撤销已确认的发布结果。
`artifact_published_result_invalid` 表示工作区已发布、但响应编码失败；诊断保留 `transaction_status: "committed"`、
编码原因和已产生的警告，`retry_safe` 为 `false`。先读取已发布的工作区，再决定是否重新导出。

若本次操作的公共恢复层新恢复了旧事务磁盘并保留崩溃前的未确认内存快照，import 结果额外包含
`warnings: ["durable_disk_restored_memory_preserved"]`：原磁盘状态已恢复，journal、磁盘备份和
内存快照继续保留，旧事务不再自动覆盖后续编辑。此提示不表示内存恢复完成，也不把旧失败改为成功；
此提示描述旧事务恢复，不表示当前 import 未保存；仅扫描到先前保留的历史材料不会重复提示。
调用方无需读取或同步隐藏身份和快照。

单一 `content_graph` facet（`summary`、`structure`、`items`、`relations`、`properties`、
`diagnostics`）使用同一直接结果契约：成功结果为 `{"entries":[...]}`。`compound` 按业务类别
返回 `{"sections":{"summary":[...],"items":[...],...}}`，不把不同类别压进一个无标签数组。只有
有界部分结果才增加 `more.returned_items` 与 `more.total_items`，完整结果不含 `more`。
公开选择字段仅有 `containers`、`items`、`endpoints`、`owners`、`fields`、`roots`；优先使用
短可读别名；重复名称使用稳定数字后缀，只有跨图歧义才使用 `GraphAlias/NodeAlias`。查询面不向模型公开 GUID、hash、
cursor 或 opaque internal ID。`more` 是不完整提示；调用方通过缩小业务条件或提高有界上限重查，
不读取或回写机器 continuation。

`content_graph.diagnostics` 只读取当前已有的原生诊断，不隐式编译、运行或打开资产编辑器。
返回的 `kind="coverage"` 条目列出实际来源及 `observed/pending/stale/unavailable/not_applicable` 状态；
`kind="diagnostic"` 条目含来源、位置、严重性、代码、消息及适用细节。`severity` 仅筛选问题条目，
不隐藏覆盖状态。Niagara 共用现有编译与 Stack 检查；Blueprint 系列和其他图使用已有节点消息，
Blueprint 另给编译状态；材质读取已存在的 feature/quality 资源，函数使用已打开的原生预览；
PCG 读取保留的组件执行日志。空问题列表只表示这些来源未报告问题，不能证明从未运行的 PCG 已通过，
也不能把 pending、stale 或缺少预览资源当成成功。Niagara emitter 问题可把 `details.emitter`、
问题 `message` 和修复 `description` 分别用于 `stack_issue_fix` 现有的 `emitter_handle_id`、
`issue_id`、`fix_id` 参数；名称须唯一，隐藏身份不需要交给模型。System 级或无修复的问题仍按诊断编辑。

TextureGraph 的节点、连线和参数 mutation 已转为 dormant，普通编辑只走公共 HJSON workspace；
`graph_validate_evaluate_settle`、artifact capture 与 bake 继续作为 active 的验证、产物与过程能力，
并与 HJSON mutation 共用服务端 AssetDurable owner。该 owner 在同一次操作中读取并冻结当前资产状态，并在后续阶段或
首写前重新检查；模型不传递 settle/bake revision。bake 会在源资产未持久化、内存状态仍脏、
操作期间状态改变或目标冲突时 fail closed。`runtime_probe` 是不持久化的当前状态读取，只接受
自身正式参数。

文件 artifact 的绝对 locator、artifact id、publisher identity 与 content hash 只留在 SDK machine
envelope。模型通过 `result.artifacts` 取得 `ArtifactHandle`；需要读取时调用
`artifact.materialize("tmp/<task>/name.ext")` 保存到短项目相对路径。已有文件字节完全一致时复用；
内容不同时默认选择 `name-1.ext` 等空闲名称，不覆盖。实际路径从返回的 `ProjectFileHandle.path` 获取。
`on_conflict="error"` 要求精确路径，冲突时报告 `artifact_destination_exists`。同内容复用仍适用。
SDK 独占创建目标，复制失败清除本次创建的残缺文件；原产物和已成功的 UE 操作不受影响。
保存失败只重试同一 artifact 的 `materialize`，无需恢复、重新截图或重放生产操作。
SDK 不把原 locator 放进 payload/repr，也不自动生成需要模型搬运的 GUID/hash 文件名。

需要按 command name 调用时使用同一个 Client：

```python
result = ue.execute("editor.session", {})
```

命名方法、`Client.execute()` 和 CLI 共用相同的 Client、Protocol 与 Transport。
它们不会在 Python 侧选择业务 route、补业务默认值、重试 command，或重新判断
服务端 Result。Unicode、任意精度整数、显式 `null` 和失败均由私有协议信封无损保留；公共 Result
递归移除协议、完整性、continuation、本机路径和收据身份，UObject/用户业务字典的 key 保持原样。

## Editor startup lifecycle runner

默认连接并复用用户已经运行的 Editor。任务确实需要自行启动 owned Editor 时，使用项目
`scripts/ue/StartUaiEditorLifecycle.ps1`；不要在业务脚本里手工拼接 `RunEditor.ps1`、端口轮询或进程清理。
runner 从现有 runtime-settings bridge 取得非敏感 loopback descriptor，通过 `RunEditor.ps1` 默认启动
保留任务栏入口、不激活的最小化 Editor。`-Minimized` 显式选择默认方式，`-Visible` 显示并激活，
`-Offscreen` 才使用隐藏、离屏、unattended 模式；三者互斥。启动完成后不持续干预窗口。

startup runner 以认证后的 `editor.open_assets` 短公共结果证明 UAI command edge，并在自身 machine receipt
中比较 endpoint owner 与本次 launch 的 PID/start-time/executable identity；这些进程身份不进入 command
payload 或 public summary。两项均成立后 `uai.editor_startup_lifecycle_receipt.v1` 才能标记 `ready`。裸 TCP、
`connection probe`、进程存活或窗口出现均不能单独证明 readiness。非 ready 路径形成稳定失败码，并只清理
本次 owned process tree；启动 runner 不拥有正常退出终态。

runner 在启动前识别同一项目的既有 Editor，并以 `preexisting_project_editor` 立即结束，而不是再次启动后等待。
启动后分别跟踪启动日志出现、Editor 初始化、UAI 启动报告和认证公共探针；对应失败为
`editor_start_evidence_missing`、`editor_initialization_timeout`、`uai_startup_timeout` 与
`uai_authenticated_probe_timeout`。启动及阶段等待期限默认均为 `0`，不按耗时自动判失败；调用者显式传入正数时才启用对应期限。
进程退出、启动日志中的实际失败及身份不匹配仍正常报告。`RunEditor.ps1` 不强制关闭 Live Coding，沿用 Editor 配置；UAI 插件 C++ 修改仍须关闭 Editor 后正常构建，不使用 Live Coding。

```powershell
pwsh -NoProfile -File scripts/ue/StartUaiEditorLifecycle.ps1 `
  -UERoot <UE-install-root> `
  -ProjectPath <project.uproject> `
  -ReceiptPath tmp/<run-id>/editor-startup.json
```

`InvokeUaiCommand.py --mode runtime-descriptor` 仅向该生命周期入口投影 transport、loopback port 和 token
transport；它不输出 token，也不携带 PID、attempt 或 terminal state。

## 保存指定 Editor 资源

保持 Editor 打开时使用同步入口：

```python
result = client.editor.save_resources(resource_refs=["/Game/MyScene"])
# 业务失败也保留逐资源结果，先检查 result.payload 的 resources / remaining_dirty_resources。
result.raise_for_error()
```

CLI：`ueagentinterfacecmd exec editor.save_resources --params-json '{"resource_refs":["/Game/MyScene"]}'`。
可直接指定任意持久资产的 package/object 路径，也可取 `editor.dirty_resources()` 的 `resource_ref`。
所有已挂载内容根（包括插件）使用同一包级原生保存，不要求资产类型专用入口；未加载的现有包自动解析加载，
首次创建的内存包也可保存。object 路径规范化为 package，配置沿用 `config:engine` 等原始值。
只处理明确请求的资源及 UE 原生所属外部包、地图 persistent level 的 build data；父包 clean 时仍保存其
dirty 附属包。其他被引用资产保留原状态；空数组不保存任何资源。原生清理空包时确认磁盘文件已删除。
已持久且未 dirty 的资源返回 `unchanged`，无需依赖 HJSON 内容变化。
`resources` 逐项给出 `saved|unchanged|failed`，失败项有 `reason`；存在失败时 Result 失败并保留这些结果，
其余独立资源继续处理。`remaining_dirty_resources` 包含仍 dirty 的资源，`editor_open=true`；
未请求的配置或资产不因本次调用被保存。关闭 Editor 仍使用下面的生命周期 runner。

## Editor safe-exit lifecycle runner

生成 binding 会精确暴露 `client.editor.safe_exit(dirty_resolution,
external_witness)`，但 `external_witness` 不是普通业务参数。安全关闭 Editor 时使用项目正式
runner `scripts/ue/SafeExitLifecycle.py`；它保持 Python SDK 的单 command 转发边界，同时负责
外层进程身份、heartbeat、两阶段不可变回执和 terminal 解析。不要在业务脚本、Connection TOML
或 CLI 参数中复制这套生命周期状态。

提供 `.uproject` 和任务专属输出路径，由 runner 解析本项目唯一 Editor 及公开 SDK 连接；
普通调用无需手工取得进程身份或建立 Connection TOML。`reject` 不接受资源列表；`save` 使用重复的
`--save-resource <resource-ref>`，`discard` 使用重复的 `--discard-resource <resource-ref>`。
资源引用来自 `client.editor.dirty_resources()`，包含所有持久内容挂载根的已加载 dirty package 和
`config:engine`、`config:game` 等六类支持配置；服务端与同一公共 dirty 集合做 exact-set 比较。
保存配置保留 UE 原生层级与差异写入，并读回确认实际文件后才清除 dirty；无法确认时报告失败并保留 dirty。
丢弃不会持久化该文件的内存变更。
`--output` 位于内部协调目录之外，是本次调用的公开结果摘要；重复使用该路径会原子更新为当前结果，
不会保留上一调用的拒绝状态。内部 attempt 的两阶段回执继续保持不可变。

成功输出为 `uai.safe_exit.terminal.v1`，必须同时具有 `terminal_status=succeeded`、
`exit_requested=true`、`process_exited=true`、`force_kill=false`、`exit_code=0` 和匹配的两阶段摘要。
runner 将非零退出码或退出码不可用报告为 failed；预览世界和资产编辑器通过 UE 原生关闭顺序收尾。
dirty reject 输出 `uai.safe_exit.runner_result.v1` 且 Editor 保持运行；外部等待超时保留精确
coordination root 并返回非成功状态。`transport_disconnected` 本身不表示退出成功。

失败摘要的 `diagnostic` 保留公开结构化原因、对象、输入位置、嵌套 cause 与 unchecked；
命令拒绝来自 `Result.error.diagnostic`，已接受操作的失败来自生命周期 payload 的 `diagnostic`。
runner 不读取旧 `operation_error.detail`，也不从错误码重新生成原因。
pre-exit 回调提交成功回执失败时，尽力发布同一 attempt 的 `pre_exit_failed.json`
（`uai.safe_exit.pre_exit_failed.v1`），记录具体创建目录、编码、写入或发布阶段的诊断。
runner 验证它与退出进程回执属于同一次退出后，返回 failed 和原诊断。若故障使两种回执都无法落盘，
只能报告缺少可验证的 pre-exit 回执，不能据此断言回调未运行或某个具体 I/O 原因。

## Command discovery

不知道 command 名称时，只在 `query.command_search` 使用少量短正向关键词；关键词优先使用
稳定的领域名、对象名和动作名，不写问题句、否定条件或背景叙述。成功 payload 只含去重后的
`commands` 名称数组。选中一个或多个名称后调用 `query.command_usage`；它以 command 名称为 key，
返回 Python 最小调用示例。CLI 紧凑输出另附 `required_params`，直接从同一生成 binding 列出必填顶层参数名与类型；SDK Result、JSON stdout 和报告保持原结构。公共 import、connect 和 Result 处理不在
每项重复。参数已经明确时直接执行选中的 named method；嵌套字段、枚举或 variant 不明确时，
按需使用本地 [describe](#parameter-schemas)，不通过执行业务方法探查参数。
基础参数的 `schema_available: false` 不代表策略没有结构；返回 `variants` 时先选择相应
`--variant`。该策略仍无结构时，再查所属领域合同。
领域语义、失败和验收说明在 `docs/active/` 的相应文档中；公开 search/usage 不返回完整教程或失败目录。

```python
import uai

with uai.connect_project() as client:
    search = client.query.command_search("asset registry record")
    usage = client.query.command_usage(["asset.registry_record"])
    # usage.payload["usage"] 直接给出每个 command 的 named 最小调用。
    result = client.asset.registry_record(target="/Engine/BasicShapes/Cube.Cube")
```

需要动态调用时使用 `client.execute(command, params)`。机器版本校验由 SDK 和 wire 内部完成；
模型不输入或输出 hash、digest、fingerprint、GUID、raw wire 或 correlation identity。
参数结构按需 describe，领域行为查所属合同，不在 search/usage 结果中复制完整 schema。

CLI 走同一 Client、Protocol 和 Transport：

```powershell
ueagentinterfacecmd exec query.command.search `
  --params-json '{"intent":"asset registry record"}'
ueagentinterfacecmd exec query.command.usage `
  --params-json '{"commands":["asset.registry_record"]}'
ueagentinterfacecmd exec asset.registry_record `
  --params-json '{"target":"/Engine/BasicShapes/Cube.Cube"}'
```

## CLI

普通单次查询直接执行 CLI，参数内联，结果写到 stdout，无需临时 Python 或参数/结果文件。
默认自动发现当前本地项目；`--project` 显式指定项目，`--connection` 指定独立连接，两者互斥：

```powershell
ueagentinterfacecmd connection show
ueagentinterfacecmd --project D:/Projects/MyProject exec editor.session
ueagentinterfacecmd --connection connection.toml connection probe
ueagentinterfacecmd exec query.command.usage --params-json '{"commands":["editor.session"]}'
```

参数来源三选一：

- `--params-json '{"intent":"editor runtime inspect"}'`
- `--params-file params.json`
- `--params-stdin`

不提供参数时发送空对象。参数输入仍为 JSON，与结果显示格式独立。
`cli_params_invalid` 在连接 UE 之前返回，保留输入来源、JSON 解码原因、行列与字符偏移；
文件读取和编码失败也保留路径及原因，不回显参数正文。按诊断修正输入，不更换连接。
Windows 使用已安装的 `.exe` 入口；复杂多行 JSON 可从 stdin 或文件传入，避免 `.cmd` 等
包装器改变引号。例如已有参数文本可直接送入 `--params-stdin`：

```powershell
'{"intent":"editor runtime inspect"}' | ueagentinterfacecmd exec query.command.search --params-stdin
```

stdout 默认使用 `compact`，统一保留公开 Result 的 `ok`、`payload`、`error` 和全部内容。
有附加公开诊断时，stdout 与报告还保留顶层 `diagnostics` 数组；没有时省略该字段。
SDK 的 `Result.diagnostics` 始终可读，默认是空列表。诊断完整传递，不参与业务 payload
的字段过滤，其存在不改变 `ok` 或业务终态。

显示规则：

- 对象用缩进 `key: value`；标量列表为 `name[N]:` 后接制表符分隔的值。
- 字段一致、值均为标量的记录列表用 `name[N]{列名…}:` 表头和 TSV 行，列名只写一次；`N` 是条目数。
- 不规则或含嵌套值的列表保留逐项结构，不强制制表、不裁剪字段。
- 空对象、空数组、空字符串分别为 `{}`、`[]`、`""`。数字、布尔和 `null` 保留类型；
  有歧义的字符串、特殊键名及含换行/制表符的值用 JSON 引号与转义，其余文本是字符串。

例如以下两列之间使用实际制表符：

```text
ok: true
payload:
  assets[2]{name	class_path}:
    Cube	/Script/Engine.StaticMesh
    Sphere	/Script/Engine.StaticMesh
error: null
```

CLI 的 stdin、stdout、stderr 和报告文件统一使用 UTF-8，不继承 Windows ANSI 编码；
管道输入和结果解码均按 UTF-8 处理。此设置仅作用于 CLI 进程。
这是 CLI 阅读格式，不作为 YAML/TOML 交换协议。程序解析 stdout 时使用 `--format json`，
可放在子命令前或子命令参数中。`--report <path>` 始终保存同一公开 Result 的完整 JSON，
不受 stdout 格式影响，不生成第二种业务报告：

```powershell
ueagentinterfacecmd exec query.command.search --params-json '{"intent":"material"}' --format json
ueagentinterfacecmd exec editor.session --report session.json
```

未取得服务端 Result 的本地用法、连接、序列化或协议错误，会按选定格式向 stderr 返回错误码和
具体原因，`--report` 同样保留该失败；退出码不变。报告写入失败时保留已输出的指令结果，不能
据此重放写操作。成功的收据调用不代表操作成功，应继续检查其业务终态和错误码。

Python SDK 的 `Result`、字典/列表和传输协议 JSON 不经过此显示层，原有程序处理方式保持不变。

正常安装后直接使用 `ueagentinterfacecmd`，无需激活环境。`uai-cli` 仅保留为独立环境内的兼容别名。
尚未继承新 PATH 的宿主可使用用户 bin 中的完整路径，或 `python.exe UeAgentInterfaceCMD/tools/sdk_environment.py cli exec ...`。
经环境工具转交全局选项时使用 `cli -- --project <路径> exec ...`。
Windows 使用原生 `.exe`，避免同名 `.cmd` 包装器改变 JSON 引号；其他系统使用对应 Python 可执行文件。
需要连续处理 workspace、operation 或 artifact handle 时使用 SDK。

### Parameter schemas

选中的命令还需确认参数形状时，使用本地 `describe`，不连接 Editor：

```powershell
ueagentinterfacecmd describe animation.sequence.pose.sample
ueagentinterfacecmd describe animation.sequence.pose.sample --parameter input --pointer /properties/time_point
```

不指定 `--variant` / `--parameter` 时只列名称、类型、必填/可空、结构是否可用及已注册的 `variants`；
`--variant <variant_id>` 返回所选分支的完整 request schema、参数/结果说明和最小示例，
再加 `--parameter` 只返回该分支中所选参数的 schema。没有 variant 的命令仍按基础参数合同查询。
单独指定 `--parameter` 返回基础参数的完整 schema，
`--pointer` 可缩到所需部分。SDK 对应 `uai.describe_command(command_id, parameter="input", pointer="/properties/time_point")`，
返回普通字典；SDK 同样支持 `variant="<variant_id>"`。结构来自同一正式 manifest，包含嵌套字段、必填列表、固定值、枚举和约束；
多分支参数保留备选形状，不代表跨参数组合都成立。没有结构时明确返回 `schema_available: false`。
更新插件合同后按既有 manifest/binding 流程刷新 SDK；此入口不执行命令，也不另行校验业务输入。
输入合同错误的 `diagnostic.expected` 保留该 `keyword` 的实际要求，包括固定值、枚举、类型和边界。

稳定退出码：

| 退出码 | 含义 |
|---:|---|
| `0` | command 成功，或 connection probe 成功 |
| `2` | CLI 用法、参数或配置错误 |
| `3` | Transport/连接失败 |
| `4` | 序列化或协议错误 |
| `5` | 服务端已返回 command failure Result |

## 静态 binding 生成

静态 binding 的唯一输入是 C++ `FUeAgentImmutableCommandRegistry` 经
`FUeAgentActiveCommandManifest` 导出的正式 manifest：

```powershell
python tools/uai_binding/generate_bindings.py `
  --manifest ../Plugins/UeAgentInterface/Resources/UaiCommandManifest.json `
  --output-root cli/uai
```

generator 不扫描 C++ 源码、Markdown、旧 CommandSpec 或 Python registry，也不按
command 前缀猜测 handler。该命令从指定 manifest 显式重建 `.py` 与 `.pyi`。

## 当前验证边界

本地 E0/E1 已证明公开导入、Connection、Transport/Protocol 分层、单次 command
转发、静态 binding、CLI 同链路和无损 Result/Error 合同。E3 已使用运行中的 C++
UAI 服务验证：SDK 命名 Query 与 CLI 调用共用同一真实 command edge；
Read/Export E3 验证了公开 Query 通过 exact
QueryDescriptor 到达 production provider，semantic Export 消费同一次真实 C4
snapshot，经 C5 生成 workspace 并由 C8F 发布；旧 `/api/uai/reference` 与
`/api/uai/export` route 不再是 active 或 fallback 入口。尚未进入 manifest 的旧
能力不属于公开 SDK。
