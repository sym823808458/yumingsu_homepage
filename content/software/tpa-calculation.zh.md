## 从激发态计算到双光子吸收分析

这套工作流连接 Gaussian、Multiwfn 与 MATLAB，用于提取激发态相关的跃迁偶极矩信息，并进行双光子吸收（TPA）批量计算与分析。

## 三个步骤

- 使用 Gaussian 计算激发态并准备相关输出文件。
- 使用 Multiwfn 提取跃迁偶极矩等信息。
- 使用 MATLAB 脚本处理提取结果并计算 TPA。

## 仓库内容

仓库提供 Gaussian 输入示例、Multiwfn 分析结果示例、批处理脚本 `batchTDM.bat` 与 MATLAB 程序 `calculateTPAinbatchpar.m`。

## 使用前提

需要自行准备 Gaussian、Multiwfn 和 MATLAB 环境。计算结果依赖所选理论方法、激发态范围及参数，请结合原始方法和仓库中的参考文献使用。

## 相关研究

该工具页与双光子吸收机器学习、纳米石墨烯和金属有机层的相关研究相连接；具体方法与引用请参见[仓库说明](https://github.com/sym823808458/calculateTPAbyMATLAB)。
