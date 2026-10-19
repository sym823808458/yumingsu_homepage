## 把量子化学结果整理成特征矩阵

MultiwfnMLhelper 是一个 Python 辅助工具，用于批量调用 Multiwfn 提取分子描述符，并将结果整理为可用于机器学习的 CSV 表格。

## 输入与输出

- 输入：一组 Gaussian 格式化检查点文件（`.fchk`）。
- 分析：通过 Python 与批处理参数组织 Multiwfn 分析。
- 输出：分子描述符 CSV 特征矩阵。

## 使用方式

从[仓库](https://github.com/sym823808458/MultiwfnMLhelper)获取 `MultiwfnMLhelper.py`、批处理脚本和参数文件。安装所需 Python 依赖，并单独准备 Multiwfn，按说明配置后运行。

## 适用范围

适合从已有波函数计算结果中批量生成描述符。它是数据准备辅助程序，不替代量子化学计算，也不代表 Multiwfn 本体；描述符定义与分析方法应同时参考 Multiwfn 原始说明。
