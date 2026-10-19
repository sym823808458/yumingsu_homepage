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

## 增加论文

在 `data/publications.json` 增加一个对象。必填字段：`id`、`title`、`authors`、`venue`、`details`、`year`、`citations`、`type`；可选 `doi`、`url`、`featured`。

`type` 可选 `journal`、`preprint`、`resource`。没有 DOI 时提供真实 `url`；两者都缺失时生成 Scholar 标题检索链接。`id` 必须唯一且采用稳定的英文字母、数字、连字符。`featured` 控制“代表作”筛选。

所有记录的引用数按同一个 Scholar 快照日期维护；不要只更新日期却保留无法追溯的旧数字。若下一次只新增论文，先明确其引用快照的日期和口径，再更新相应记录。

`authors_verified` 是出版元数据核对后的完整作者列表；若存在，页面优先使用它，否则使用 `authors`。DOI 与作者数据优先核对出版商或 Crossref，具体来源字段可随记录保存。

`tools/verify_metadata.py` 是可选联网审计工具，会修改论文数据，不参与正常构建。仅在确需核对书目信息时手动运行，并检查差异；API 限流或查询失败不能视为核验成功。

## 增加软件

1. 在 `data/software.json` 增加软件条目，遵循已有结构。
2. 为软件设置唯一、稳定的 `slug`，如 `my-tool`。
3. 新建 `content/software/my-tool.zh.md` 与 `my-tool.en.md`。
4. 运行构建。英文页面自动生成到 `software/my-tool/`，中文页面生成到 `zh/software/my-tool/`。旧 `en/software/my-tool/` 自动跳转到英文入口。
5. 实际实现与计划功能分开表述；下载、文档和源码链接均需可用。

当前 Markdown 支持段落、`##`/`###` 标题、`-` 列表、`**粗体**`、行内代码和 HTTPS 链接；不支持任意 HTML、表格或复杂 Markdown 扩展。需要扩展语法时，修改构建器并检查所有页面。

## 语言与入口约定

- 网站根路径默认显示英文，不按浏览器语言自动跳转。中文版本位于 `zh/`。
- 页面右上方的“中文 / English”按钮切换对应页面，软件子页切换后保留当前项目，主页切换后保留当前章节锚点。
- 默认英文名称使用软件条目的 `name_en`；中文名称使用 `name_zh`，缺失时使用通用 `name`。中文关键词可通过 `tags_zh` 单独维护。
- 导航、简介、研究方向、软件说明、筛选和提示文字均有中文版本；软件品牌、代码命令、论文标题、作者、期刊名和 DOI 保留原文。用户已明确不需要论文标题中文译名。
- 旧 `en/` 页面由构建器生成兼容跳转，保留 URL 查询参数和章节锚点；不要手动删除这些页面。
- 样式和脚本链接包含由文件内容生成的版本标识，修改后构建即可更新，避免访客继续使用旧缓存。

## 发布与域名

现有项目地址为 `https://sym823808458.github.io/yumingsu_homepage/`。所有本地资源采用相对路径，以兼容项目路径和将来的独立域名。

绑定域名时，在注册商配置 DNS，在 GitHub 验证域名所有权，再配置 Pages 自定义域名和 HTTPS。只在确认可用后添加对应 `CNAME`。不要把域名注册截图当作 DNS 已生效的证据。

## 回滚

使用 `git log` 找到需要撤销的发布提交，通过 `git revert <commit>` 生成回滚提交，再推送。不要使用强制推送改写公开历史。网站源码和生成页面在同一提交中，可以一起恢复。

## 访问量与下载量

本次没有接入第三方网站统计。仓库 Traffic、Pages 网站访问和 Releases 附件下载属于不同统计口径。今后接入真实统计服务时，记录服务名称、账户归属、接入位置和统计口径；不要把客户端公开页面中的数值误当作真实用户数。
