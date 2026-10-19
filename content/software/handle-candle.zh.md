## 围绕科学问题持续推进文献调研

秉烛夜读是一个 Windows 本地文献调研工具。它通过 Edge 打开文献页面，读取可获取的页面内容，并交给大语言模型分析，服务于多轮、可追溯的科研调研。

## 主要流程

- 根据研究问题进行文献检索与相关性分析。
- 读取页面内容并组织结构化分析结果。
- 沿引用关系扩展调研，保存 URL、日志与报告。
- 结合 Zotero 整理和下载本人有权访问的文献。

## 本地运行

从仓库下载代码，安装 `requirements.txt` 中的依赖，运行 `python modular_research_gui.py` 启动主界面。PDF 文件夹分析可使用 `python pdf_analysis_gui.py`。

该工具依赖 Windows、Microsoft Edge、Python 及所选模型服务；PDF 下载流程需要 Zotero。模型调用可能产生服务商费用，访问全文取决于用户已有的文献权限。

## 代码与反馈

[源码仓库](https://github.com/sym823808458/handle_candle)提供安装脚本、使用说明和问题反馈入口。
