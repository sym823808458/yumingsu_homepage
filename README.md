# Yuming Su / 苏禹铭 — Academic Website

个人学术主页，托管于 GitHub Pages。**默认入口为英文**（`index.html`），中文入口为 `zh/index.html`。页首的“中文 / English”按钮切换当前页面的语言。

英文软件页位于 `software/<slug>/`，中文软件页位于 `zh/software/<slug>/`。旧的 `en/` 地址保留为跳转入口。论文标题、作者、期刊名和 DOI 在两种语言下均保留原文，不添加论文标题译名。

当前地址：https://sym823808458.github.io/yumingsu_homepage/

## 日常更新入口

| 更新内容 | 编辑文件 |
| --- | --- |
| 个人简介 | `content/about.zh.md`、`content/about.en.md` |
| 职位、单位、研究方向、经历、Scholar 统计 | `data/profile.json` |
| 论文、引用快照、DOI、代表作标记 | `data/publications.json` |
| 软件目录、链接、简介 | `data/software.json` |
| 软件详细介绍 | `content/software/<slug>.zh.md`、`<slug>.en.md` |
| 各软件累计访问（GoatCounter） | `data/analytics.json`，启用方法见 `MAINTENANCE.md` |
| 页面框架、视觉、交互 | `templates/base.html`、`assets/site.css`、`assets/site.js` |

修改内容后，用 Python 3.10+ 运行（无需安装依赖）：

```text
python tools/build.py
python tools/build.py --check
python tools/check_site.py
python -m http.server 8765 --bind 127.0.0.1
```

预览 http://127.0.0.1:8765/ ，检查中文、英文、软件子页和手机布局。将内容源文件与生成的 HTML 一起提交到 `main`，现有 GitHub Pages 从仓库根目录发布。不要只修改生成的 HTML。

详细操作见 [MAINTENANCE.md](MAINTENANCE.md)，内容证据见 [SOURCES.md](SOURCES.md)。

## 设计原则

- 静态网站；不依赖后端、数据库或付费构建服务。
- 内容集中维护，同一模板生成中文、英文和软件页。
- 论文默认显示引用最高的 10 篇，可切换为按时间展示收录的期刊论文与预印本；禁用 JavaScript 时仍显示前 10 篇。
- 英文字体优先使用系统 Times New Roman，中文使用宋体等衬线字体回退；样式、脚本和照片本地托管，不依赖外部字体服务。
- 学术统计注明快照日期，记录条目数与全部论文数分开理解。
- 域名购买与绑定分开进行；未确认 DNS 配置前不创建 `CNAME`。

## 作者与资料

Yuming Su / 苏禹铭。论文版权归原权利人；网站提供出版商、DOI、预印本或软件资源链接，不复制论文全文。
