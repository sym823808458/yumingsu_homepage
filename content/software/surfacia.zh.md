## 让分子表示保留化学意义

Surfacia 将分子表面性质转化为多层级描述符，并连接特征筛选、机器学习与 SHAP 解释。它面向希望将预测结果与化学结构联系起来的研究者。

## 工作流程

- 从 SMILES 与分子结构准备开始，组织量子化学与表面分析任务。
- 提取静电势、局部离子化能等表面性质及相关描述符。
- 进行特征筛选、建模与模型解释。

## 在服务器上运行描述符表格

点击上方**在线计算演示**。已批准用户与 GBLine 共用同一个账户提交 Surfacia 任务。当前 HTTPS 入口为临时地址，可能变更；新用户的邮箱验证仍需作者完成 QQ 发信配置，已有的批准账户可使用计算服务。

- 在计算页下载示例 CSV，或准备自己的 UTF-8 CSV：包含一个连续数值的 `target` 列，以及 1–32 个数值描述符列；30–500 个样本，文件不超过 2 MiB。描述符列名以英文字母开头，只使用字母、数字和下划线；不接受空值、无穷值或公式。
- 可选的 `Sample Name` 列填写唯一编号，只使用字母、数字、点、下划线和连字符，并以字母或数字开头；省略时使用行号。可选的 `smiles` 列仅作为文本接受，本次在线计算忽略结构内容；其余列均作为数值描述符。
- 用邮箱和密码注册，验证邮箱并等待管理员批准。登录后选择 **Surfacia**，上传 CSV 并提交。保留任务编号；可以关闭页面，之后重新登录查看进度。
- 完成后下载 ZIP。先阅读 `README.txt` 和 `report.json`，再检查 `predictions.csv` 与 `parity.png`；结合训练集均值基线，判断独立测试的 MAE、RMSE、R²，再解释特征。
- `feature_importance.csv` 和 `shap_importance.png` 展示影响幅度；`shap_values.csv` 保留测试样本的描述符值与带正负号贡献，`shap_dependence.png` 展示首要描述符的方向。SHAP 解释的是拟合模型，不能直接证明化学机制或因果干预效果。

两个工具共用每个账户的配额：同时运行 1 个任务、排队 2 个任务、每日提交 10 次。Surfacia 单次最长 10 分钟；结果仅提交账户可下载，72 小时后删除，请及时保存。

### 在线版具体计算什么

服务器调用 Surfacia 4.0.0 的 `BaseChemMLAnalyzer.XGB_Fit`，使用全部上传描述符及固定 XGBoost 回归参数：350 棵树、深度 8、学习率 0.03，仅使用 CPU。仅接受数据，不接受用户脚本或模型。

固定随机种子 42，留出 20% 的不同描述符向量作为测试组；相同向量保持在同一组。建模池采用五折分组验证，每个建模样本均得到一次折外预测；随后用整个建模池训练最终模型，对未参与训练的测试样本预测并计算带符号 TreeSHAP，同时核对贡献加和是否还原预测值。不进行特征搜索、调参、早停或按测试结果挑选模型。下载包记录参数、特征顺序、依赖版本、输入与训练源码哈希、数据划分及最终 XGBoost 原生 `model.json`。

这是有计算上限的网页分析流程，与桌面 CLI 的重复随机划分、文章冻结的研究评估方案分别说明。随机分组不能替代骨架划分、时间划分或外部验证。完整结构准备、量化计算、表面描述符提取和交互式三维查看仍在本地流程中进行。

### 已完成的在线案例

2026 年 10 月 20 日，36 个公开分子的 CSV 已完成真实网页提交、后台计算和 ZIP 下载。28 个建模样本的折外 R² 为 0.776、MAE 为 0.259；8 个留出样本的 R² 为 0.858、MAE 为 0.181、RMSE 为 0.275，训练集均值基线的测试 RMSE 为 0.762。SHAP 贡献加和还原预测值的误差不超过 3.6 × 10⁻⁷。

[下载示例 CSV](http://yumingsu.top/downloads/surfacia/descriptors.csv)与[本次运行完整输出](http://yumingsu.top/downloads/surfacia/online-demo-results.zip)。示例使用 6 个 RDKit 描述符和**计算 Crippen logP**，不涉及实验标签或量化表面描述符。测试集很小，划分方案也与桌面教学不同，不能据此直接比较优劣；特征排序仅描述本次运行。

## 安装与使用

通过上方命令从 PyPI 安装当前版本，再运行 `surfacia --help` 查看命令；已有描述符表时，可以单独进行机器学习分析。

4.0.0 已在 PyPI 发布，聚焦描述符、建模与解释。如果此前安装了 3.0.3，请使用上方升级命令，并查看手册的迁移说明。[解释案例](https://surfacia.readthedocs.io/zh-cn/latest/zh/examples/interpretation.html)从硫局部的化学问题讲到证据卡，并用可下载教学运行的实际带符号 SHAP 输出示范读图。

完整量子化学流程还依赖 xTB、Gaussian 和 Multiwfn 等外部软件，需要自行安装并满足相应许可要求。环境与版本要求请以当前手册为准。

## 研究预印本

Yuming Su, Yangtao Chen, Yiheng Dai and Cheng Wang. **Explain and Go Beyond with Surfacia: A Surface-Descriptor based Workflow for Interpretable Molecular Machine Learning.** ChemRxiv，v1，2026 年 8 月 27 日。[DOI: 10.26434/chemrxiv.15007949/v1](https://doi.org/10.26434/chemrxiv.15007949/v1)。

这篇归档预印本早于当前 4.0.0 的范围调整及最新可解释性稿件。标题按登记原文保留，不作为当前功能列表，也不表示期刊已经接收。

## 手册与源码

[阅读完整中文手册](https://surfacia.readthedocs.io/zh-cn/latest/zh/index.html)或访问[源码仓库](https://github.com/sym823808458/Surfacia)，查看命令、示例、依赖与问题反馈入口。
