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

论文区只展示 `journal` 与 `preprint`：默认按引用降序显示前 10 篇；“按时间”显示全部收录论文，以年份降序排列，同年按引用排序。`resource` 仍保留在数据文件中，不混入论文排名。完整学术列表链接到 Scholar。生成 HTML 已设置默认隐藏状态，无 JavaScript 时也只显示前 10 篇。软件页链接到前 10 篇之外的论文时，脚本会自动切到时间视图并定位该论文。

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

GoatCounter 接入代码已准备，配置集中在 `data/analytics.json`。当前 `enabled: false`，尚未开始采集；没有配置时软件详情页显示“尚未启用”，不会显示假的零值。

启用步骤：

1. 作者在 https://www.goatcounter.com/signup 创建本人账号和站点，域名填 `yumingsu.top`。保留默认 Sessions 会话统计。
2. 在站点设置启用 **Allow adding visitor counts on your website**，允许读取公开计数；管理后台不必公开。
3. 把公开站点地址（例如 `https://your-code.goatcounter.com`，不包含 `/count`）填入 `endpoint`，将 `started_on` 填为实际启用日期，`enabled` 改为 `true`。不需要 API token、密码或服务器。
4. 构建并发布，检查 `/software/<slug>/` 的真实计数、中文对应页和 GoatCounter 后台。第一次没有统计或被拦截时可显示“暂时无法读取”；服务响应可能缓存数小时，不应靠反复刷新验收。

英文和中文软件页都记录到 `/software/<slug>/`；域名、旧项目路径、`index.html`、参数和锚点不会拆散同一软件。主页展示当前可见软件各自的累计访问，但仅打开主页不会增加这些软件的计数。`allowed_hosts` 防止本地预览采集。

这是启用后的**会话访问次数**，不是历史独立人数；同一人跨会话可能重复计数，语言切换在同一会话合并。启用前没有记录的访问无法补回。源码仓库 Traffic、手册访问、PyPI 安装和 Release 下载不计入个人主页软件页访问。广告拦截器、脚本禁用等也可能造成漏计。禁止从 localStorage、随机数或示意数字生成所谓访问量。

官方接入与口径：https://www.goatcounter.com/help/start 、https://www.goatcounter.com/help/visitor-counter 、https://www.goatcounter.com/help/sessions 。需要保存长期历史时，可在作者后台导出 CSV，不能把访问量冒充下载量。

## 在线计算入口

软件条目的 `online.url` 统一保存实际计算平台入口，`online.note.en/zh` 同步注明临时状态、注册条件和发信配置是否就绪。入口按钮由模板生成，使用方法保存在对应的 Markdown 中。正式接入 compute.yumingsu.top 后，只更新数据文件中的 URL 和真实状态；不要将服务器配置、队列数据库、上传文件、测试账户或密钥复制到公开仓库。在线算法版本、评估方案和资源限制必须与实际部署一致。
