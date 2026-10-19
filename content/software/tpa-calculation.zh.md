## 从激发态计算到双光子吸收分析

这套工作流连接 Gaussian 激发态计算、Multiwfn 跃迁偶极矩提取与 **Python 或 MATLAB** 后处理，用于双光子吸收（TPA）光谱和截面的批量计算。

## 三个步骤

- 完成 Gaussian TD 计算，用 `formchk` 将检查点转为 `.fchk`。
- 用 Multiwfn 导出跃迁偶极矩文本，每个分子保存为单独命名的 `.txt`。
- 选择 Python 或 MATLAB 处理同一类型的导出数据，生成数值光谱。

## Python 配套版本

已有的配套脚本 `tpa_from_multiwfn.py` 读取 Multiwfn 文本中的基态偶极矩、基态到激发态及激发态之间的跃迁矩和激发能。输入是导出的偶极矩文本，不是直接读取 Gaussian 原始日志。

通过上方联系入口获取 Python 配套程序后：

- 创建环境：`conda create -n tpa python=3.11`，然后运行 `conda activate tpa`。
- 安装两个依赖：`python -m pip install numpy matplotlib`。
- 将导出的文本放入脚本旁的 `tpa_inputs` 文件夹，运行 `python tpa_from_multiwfn.py --input-dir tpa_inputs --output-dir tpa_outputs --plot`。

程序生成 `tpa_summary.csv`、每个分子的 `*_tpa_spectrum.csv`，以及可选的 `plots/` 光谱 PNG。Python 后处理不需要 MATLAB；重新生成电子结构与偶极矩输入仍需要上游量化软件。

## MATLAB 路线

[公开 MATLAB 仓库](https://github.com/sym823808458/calculateTPAbyMATLAB)提供 Gaussian 与 Multiwfn 示例、`batchTDM.bat` 和 `calculateTPAinbatchpar.m`。它保留为原工作流的公开源码入口；Python 配套版本目前通过联系单独获取。

## 输出与结果核对

Python 输出中的 `sigma_gm` 为计算截面，单位 GM；`lambda2_nm` 是简并双光子激发的入射波长，`lambda_half_nm` 为其一半，即单光子等效波长。绘图和报告峰值时应明确使用哪一种波长。

Python 与 MATLAB 路线均用于既有计算流程的后处理。切换实现时请用已知输入交叉核对，目前未认证二者数值完全等价。结果依赖输入电子态、跃迁矩、态数范围与展宽参数。

## 相关研究

该工具页与双光子吸收机器学习、纳米石墨烯和金属有机层的相关研究相连接；具体方法与引用请参见[仓库说明](https://github.com/sym823808458/calculateTPAbyMATLAB)。
