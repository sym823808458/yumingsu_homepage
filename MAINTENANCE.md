# 网站维护说明

## 一次普通更新

1. 拉取远程最新版本，查看 Git 状态，保留已有未提交改动。
2. 按 README 的表格修改内容文件；日常更新不需要修改 HTML 或 CSS。
3. 在 `data/profile.json` 中更新页面更新日期；若更改学术统计，单独更新 `scholar_snapshot.date`。
4. 运行 `python tools/build.py`、`python tools/build.py --check`、`python tools/check_site.py`。
5. 本地预览，检查有改动的页面和相关链接。
6. 把源文件和生成页面一起提交、推送到 `main`。现有 GitHub Pages 发布仓库根目录。
7. 等待 Pages 构建完成，检查线上内容。

无需长期运行本地 HTTP 服务；预览结束后可以关闭。Python 只在生成页面时需要，GitHub 上发布的是静态文件。

## 研究方向图片

主页研究方向采用三行图文布局，手机上先显示方向说明，再显示完整图片。每个 `data/profile.json` 的 `research` 条目通过 `publication_id` 关联已有论文，并用 `figure` 保存本地图路径、固有尺寸、中英文替代文字与说明、来源页面、作者/期刊/图号和许可链接。替换图片时同步这些字段；图片保持完整比例，点击可打开完整文件。原图保存在 `images/research/`，无需外部图片服务。

只使用已发表且已核对复用许可的图片。综述中转载其他团队的图片不自动适用整篇文章的许可，也不能作为本人搭建设备的展示。现有原图、许可与下载来源见 `images/research/README.md`。英中文共用原始英文论文图，不重绘或翻译图内文字。

## 增加论文

在 `data/publications.json` 增加一个对象。必填字段：`id`、`title`、`authors`、`venue`、`details`、`year`、`citations`、`type`；可选 `doi`、`url`、`featured`。

`type` 可选 `journal`、`preprint`、`resource`。没有 DOI 时提供真实 `url`；两者都缺失时生成 Scholar 标题检索链接。`id` 必须唯一且采用稳定的英文字母、数字、连字符。旧 `featured` 字段保留为元数据，不再控制前台展示。

论文区只展示 `journal` 与 `preprint`：默认显示 10 篇：有明确 `display_priority` 的作者确认论文优先，按该字段升序；其余按引用数降序补齐。不再提供“按时间”切换。`resource` 仍保留在数据文件中，不混入论文排名。完整学术列表链接到 Scholar。生成 HTML 已设置默认隐藏状态，无 JavaScript 时也只显示前 10 篇。软件页链接到默认列表外的论文时，脚本只显示该目标条目并定位，不改变排序。

所有记录的引用数按同一个 Scholar 快照日期维护；不要只更新日期却保留无法追溯的旧数字。若下一次只新增论文，先明确其引用快照的日期和口径，再更新相应记录。

`authors_verified` 是出版元数据核对后的完整作者列表；若存在，页面优先使用它，否则使用 `authors`。DOI 与作者数据优先核对出版商或 Crossref，具体来源字段可随记录保存。

`tools/verify_metadata.py` 是可选联网审计工具，会修改论文数据，不参与正常构建。仅在确需核对书目信息时手动运行，并检查差异；API 限流或查询失败不能视为核验成功。

## 增加软件

1. 在 `data/software.json` 增加软件条目，遵循已有结构。
2. 为软件设置唯一、稳定的 `slug`，如 `my-tool`。
3. 新建 `content/software/my-tool.zh.md` 与 `my-tool.en.md`。
4. 运行构建。英文页面自动生成到 `software/my-tool/`，中文页面生成到 `zh/software/my-tool/`。旧 `en/software/my-tool/` 自动跳转到英文入口。
5. 实际实现与计划功能分开表述；下载、文档和源码链接均需可用。

对于尚未公开发布源码的软件，可以不填 `repository`，设置 `contact: true`，页面会使用个人邮箱作为联系入口。可用 `status`、`availability` 的中英文字段注明开发阶段和获取方式，不要创建虚假的仓库或下载链接。

不再展示的软件设置 `visible: false`。条目与 Markdown 保留归档，主页不再列出或读取其计数，中英文详情页与旧英文地址转到对应语言主页的软件列表并标记 noindex。恢复展示时移除该字段或改为 `true` 后重新构建。

软件按 `data/software.json` 的顺序展示；GBLine 为第二个可见条目。已核实的论文预印本可用 `preprint` URL 添加按钮，并在中英文 Markdown 说明版本与发表状态；不能把论文 DOI 当作软件发行包 DOI，也不能把本地初稿写成公开预印本。

项目条目可添加 `media` 数组展示图片或动画。每项包含 `type`（`image` / `animation`）、`src`（相对资源路径，或按 `en` / `zh` 区分的路径）、`width`、`height`，以及中英文 `alt`、`caption`；动画另需中英文 `label`，默认收起，由访客主动展开。只添加已确认适合公开的演示资源，并注明示意图、模型输出与实测结果的区别。

横向流程图可另设 `mobile_src`、`mobile_width`、`mobile_height`，在手机上显示竖向版本，避免把整张图缩成无法阅读的小字。

当前 Markdown 支持段落、`##`/`###` 标题、`-` 列表、`**粗体**`、行内代码和 HTTPS 链接；不支持任意 HTML、表格或复杂 Markdown 扩展。需要扩展语法时，修改构建器并检查所有页面。

## 语言与入口约定

- 英文字体优先使用 Times New Roman，中文回退到系统宋体等衬线字体。当前照片是作者于 2026-10-19 提供的竖版发言照片，原文件保存为 `images/profile.jpg`；通过 `object-fit: cover` 适应相框，与姓名区域对齐，不再使用旧照片的放大裁切规则。更换照片时同步 `tools/build.py` 中的固有尺寸；图片地址自动附带内容哈希，避免旧缓存。不要用图片生成重画本人照片。

- 网站根路径默认显示英文，不按浏览器语言自动跳转。中文版本位于 `zh/`。
- 页面右上方的“中文 / English”按钮切换对应页面，软件子页切换后保留当前项目，主页切换后保留当前章节锚点。
- 默认英文名称使用软件条目的 `name_en`；中文名称使用 `name_zh`，缺失时使用通用 `name`。中文关键词可通过 `tags_zh` 单独维护。
- 导航、简介、研究方向、软件说明、筛选和提示文字均有中文版本；软件品牌、代码命令、论文标题、作者、期刊名和 DOI 保留原文。用户已明确不需要论文标题中文译名。
- 旧 `en/` 页面由构建器生成兼容跳转，保留 URL 查询参数和章节锚点；不要手动删除这些页面。
- 样式和脚本链接包含由文件内容生成的版本标识，修改后构建即可更新，避免访客继续使用旧缓存。

## 发布与域名

现有项目地址为 `https://sym823808458.github.io/yumingsu_homepage/`。所有本地资源采用相对路径，以兼容项目路径和将来的独立域名。

自定义域名配置为 `yumingsu.top`，由仓库根目录的 `CNAME` 文件维护。2026-10-19 已通过实时 DNS 查询确认四条 GitHub Pages A 记录与 GitHub 所有权验证 TXT 记录；内容更新时保留 `CNAME`，不要重新添加或购买服务器。注册截图不能替代 DNS 查询。

发布后检查 `https://yumingsu.top/` 和软件子页，再到仓库 Settings → Pages 确认自定义域名和 Enforce HTTPS 状态。域名所有权 TXT 验证、仓库自定义域名绑定、HTTPS 证书签发是不同步骤；只完成 TXT 验证不会让网站自动使用域名。若启用 `www.yumingsu.top`，需在注册商另加 `www` CNAME 指向 `sym823808458.github.io`（不包含协议或仓库路径）。

## 回滚

使用 `git log` 找到需要撤销的发布提交，通过 `git revert <commit>` 生成回滚提交，再推送。不要使用强制推送改写公开历史。网站源码和生成页面在同一提交中，可以一起恢复。

## 访问量与下载量

2026-10-21 起改用作者现有 Cloudflare 账号中的 Worker / D1，配置集中在 `data/analytics.json`：provider 为 `cloudflare-d1`，endpoint 为 `https://stats.yumingsu.top`，enabled 为 true。无需 GoatCounter 账号、网站访客注册或前端密钥。静态主页继续由 GitHub Pages 发布；统计服务与 B650 计算服务相互独立。

主页展示六个可见软件各自的累计详情页访问及六项合计，打开主页只读取计数，不增加各项计数。英语、中文、`index.html`、查询参数和片段在同一软件下合并；旧 `/en/` 入口先跳转，再由正式详情页计数。隐藏的 MultiwfnMLhelper 不统计。中英文对应页不翻译论文标题。

计数口径为**同一标签页内、同一软件，从一次事件开始的 30 分钟内合并计次**。脚本在 sessionStorage 中暂存随机事件 ID、窗口开始时间和确认状态，再提交固定 software / event_id；只有进入新窗口才生成新事件。刷新和语言切换保留同一事件。请求在服务端成功但响应丢失时，重试同一 ID 不会重复增加。软件之间的计数分别维护。无法使用 sessionStorage 或随机数 API 时只读取累计值，以免无法去重的刷新增加计数。

这是**软件详情页访问次数**，不是独立访客人数、下载量或算法执行次数。跨标签页、浏览器或 HTTP/HTTPS origin 可能分别计次；脚本禁用、广告拦截和网络失败可能漏计。公开接口的 Origin 校验不是身份认证，尽力限流也不能完全防刷量。此前未采集的历史访问无法补回，不提供虚假的历史数字。正常维护验收对线上页面的访问也可能计入。

D1 只保存六项累计值、数据库初始化时间和临时随机去重事件，不保存邮箱、任务、科研数据或原始 IP；Cloudflare 平台日志由作者控制台的 Observability 设置管理，与 D1 表是两回事。计数读取失败显示“暂时无法读取”，不能替换成零或随机数。所有累计量从服务端读取，浏览器本地不保存所谓累计总数。

维护入口：

- Cloudflare → Workers & Pages → `yumingsu-visits` → Domains：应绑定恰好 `stats.yumingsu.top`。如果输入框自带 `.yumingsu.top` 后缀，只填 `stats`，避免重复主域名。用 Custom Domain，DNS 和证书由 Cloudflare 处理。
- Worker 的 D1 绑定变量为大写 `DB`，数据库为 `yumingsu-visits`；不要改成其他变量名。
- `https://stats.yumingsu.top/health` 检查数据库连通；`/v1/counts` 读取六项和合计，GET 不增加计数。
- 重跑初始化 schema 不会清零；不要删除 D1 数据库或手工改累计数字。后续可按官方 D1 导出流程备份。
- 新增或隐藏软件时，要同步 Worker、schema、`assets/analytics.js` 和构建器的固定软件名单；不要只改前端。
- 本地验证：`node --test tools/test_analytics.mjs`、正常构建三项检查；预览 hostname 不在 allowed_hosts 内，禁止本地预览误采集。
- 紧急停采：将 enabled 改为 false，重新构建发布。保留数据库，日后恢复可继续累计。免费方案仍有 Workers / D1 配额，达到额度可能暂时不可用，不应自动升级付费。

此段替代此前尚未启用的 GoatCounter 准备方案。基础构建没有增加任何依赖或新框架。

## 在线计算入口

软件条目的 `online.url` 统一保存实际计算平台入口，`online.note.en/zh` 同步注明临时状态、注册条件和发信配置是否就绪。入口按钮由模板生成，使用方法保存在对应的 Markdown 中。正式接入 compute.yumingsu.top 后，只更新数据文件中的 URL 和真实状态；不要将服务器配置、队列数据库、上传文件、测试账户或密钥复制到公开仓库。在线算法版本、评估方案和资源限制必须与实际部署一致。

### 固定计算入口（2026-10-21）

GBLine、Surfacia、风压筛查及 TPA 的入口统一为 `https://compute.yumingsu.top/?tool=<tool>`，tool 分别为 gbline、surfacia、wind、tpa。已通过正式域名下的注册、邮箱验证、管理员审批、密码登录、四工具提交及结果下载验收。验收邮件私密捕获，不向测试地址发送；QQ SMTP 由作者配置并确认收到真实测试邮件。

公开页面不再显示临时地址或 SMTP 待配置。计算服务器当前运行，但尚未配置虚拟机与正式隧道的开机自启；域名固定不表示 24 小时可用。学术主页 GitHub Pages 的 HTTPS 证书仍待签发，计算入口证书已在浏览器验证。服务器端备份和身份凭据只保存在私有部署目录，不在此仓库维护。

主页软件列表根据 `online` 配置显示直达计算平台的免费体验标签；文字由 `online.label.en/zh` 集中维护。只有实际有在线入口的软件才显示该标签；注册、邮箱验证与审批条件在列表上方说明。

### 作者身份与优先展示（2026-10-21）

作者此次确认七篇优先论文（六篇原有论文与新补充的 19F NMR 共同通讯论文），通过 `author_roles`（first / co_first / corresponding / co_corresponding）、`author_role_source` 和唯一 `display_priority` 维护。旧 `featured` 不是作者身份凭据，不用于排序。按作者提供的顺序排列这七篇，其余按旧引用快照补齐至十篇；新论文未知引用数保存为 null，显示破折号及“未记录”，不填零，也不刷新未重新核对的 Scholar 总量与快照日期。
