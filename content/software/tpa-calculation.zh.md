## 从激发态计算到双光子吸收分析

这套工作流基于 **sum-over-states（SOS，态求和）理论**，由电子激发能和偶极矩矩阵元计算双光子吸收（TPA）光谱与截面。工作流连接 Gaussian 激发态计算、Multiwfn 跃迁偶极矩提取与 **Python 或 MATLAB** 后处理。

## 理论依据：sum-over-states（SOS，态求和）

在电偶极近似下，SOS 理论利用激发能、偶极矩矩阵元及含频率的能量分母，对电子态求和，得到非线性光学响应。对于简并双光子吸收，两个同频光子共同提供激发所需的能量；中间态求和描述的是虚跃迁通道，并不表示依次占据两个真实电子态的逐步吸收。

后处理代码使用输入的有限组电子态和唯象阻尼，计算随频率变化的**二阶超极化率 γ**，即分子的三阶光学响应，再由取向平均后响应的虚部得到 TPA 光谱及以 GM 为单位的截面。计算链条为**激发能与偶极矩 → SOS 响应 → 取向平均 → TPA 截面**。这是基于电子结构的理论计算；相关论文中的 ML-TPA 性质预测模型属于另一条研究路线。

原始 MATLAB 仓库明确将 **Terenziani 等人（2008）**列为计算方法参考；**Orr 和 Ward（1971）**给出了非线性光学响应的微扰 SOS 理论基础；**Göppert-Mayer（1931）**是双光子跃迁理论的奠基文献。完整书目信息与 DOI 见下方。

## 在线计算：上传两个文件

进入[双光子吸收计算工作台](https://fragrance-were-swim-round.trycloudflare.com/?tool=tpa)，使用已批准的账户登录，选择 TPA，上传同一次 Gaussian 计算的 **`.fchk` + TD `.log`** 后提交。服务器自动运行固定的 Multiwfn 导出和 Python SOS 后处理；任务记录中可查看光谱、偶极矩参考核对表并下载 ZIP。排队后可以关闭网页。

输入应来自已正常结束的全电子、限制性闭壳层单重态 TD 计算，包含 **IOp(9/40=4)** 和 2–40 个单重激发态。请事先用 Gaussian `formchk` 转换检查点。fchk 最大 64 MiB，log 最大 16 MiB；当前限制为 300 个原子、2000 个基函数。服务检查原子顺序、几何、坐标轴／原点、态数和能量，不完整、不支持或不配对的输入会被拒绝。服务器不运行 Gaussian，也不优化结构。

在线服务**只接受 fchk + log 配对输入**。Multiwfn 提取与永久偶极矩定义核对由服务器完成，不需要上传导出文本或手填偶极矩向量。

当前为临时 HTTPS 地址，可能变化或停止。新用户需邮箱验证并经管理员批准；QQ SMTP 尚未配置，新注册暂时无法完成验证。每项任务最多使用 2 个 CPU 线程、4 GiB 内存，总时限 10 分钟。各工具共用每用户 1 项运行、2 项排队、每天 10 次提交的配额。私人结果保留 72 小时。

上图仅保留为数值核心的历史合成代数核对，不是可选输入方式，也不是分子精度基准。[历史核对结果](http://yumingsu.top/downloads/tpa-calculation/synthetic-results.zip)可供查阅。

## 永久偶极矩参考：先保存，再扣除

每个对角元应使用 **Δμᵢ = μᵢᵢ − μ₀₀**，且必须在改变任何对角元之前复制 μ₀₀。否则第一次循环会将基态参考清零，后续激发态就没有扣除原参考。网页版采用已修正的 Python 实现，并检查所有永久偶极矩共同平移时光谱不变。

这里固定使用的 Multiwfn 3.8(dev)、2024-10-20 版本，在 Gaussian 导出中给出基态总偶极矩和激发态电子偶极矩对角元。服务器由 fchk 核电荷与笛卡尔坐标计算核贡献，先统一为电子贡献定义，再扣除已保存的基态参考。报告和 `dipole_reference.csv` 保留原始、统一定义后及差值三组向量。核贡献接近零会如实记录，不能仅凭“仅电子贡献”的注释断言某个历史样本存在显著混用误差。

## Python 配套版本

已有的配套脚本 `tpa_from_multiwfn.py` 读取 Multiwfn 文本中的基态偶极矩、基态到激发态及激发态之间的跃迁矩和激发能。输入是导出的偶极矩文本，不是直接读取 Gaussian 原始日志。

通过上方联系入口获取 Python 配套程序后：

- 创建环境：`conda create -n tpa python=3.11`，然后运行 `conda activate tpa`。
- 安装两个依赖：`python -m pip install numpy matplotlib`。
- 将导出的文本放入脚本旁的 `tpa_inputs` 文件夹，运行 `python tpa_from_multiwfn.py --input-dir tpa_inputs --output-dir tpa_outputs --plot`。

程序生成 `tpa_summary.csv`、每个分子的 `*_tpa_spectrum.csv`，以及可选的 `plots/` 光谱 PNG。Python 后处理不需要 MATLAB；重新生成电子结构与偶极矩输入仍需要上游量化软件。

## MATLAB 路线

[公开 MATLAB 仓库](https://github.com/sym823808458/calculateTPAbyMATLAB)提供 Gaussian 与 Multiwfn 示例、`batchTDM.bat` 和 `calculateTPAinbatchpar.m`。公开版的对角元参考循环已于 2026-10-20 修正，但未认证 MATLAB 运行结果或绝对截面。它保留为原工作流的公开源码入口；Python 配套版本目前通过联系单独获取。

## 输出与结果核对

Python 输出中的 `sigma_gm` 为计算截面，单位 GM；`lambda2_nm` 是简并双光子激发的入射波长，`lambda_half_nm` 为其一半，即单光子等效波长。绘图和报告峰值时应明确使用哪一种波长。

网页版保留已核对 Python 核心的方程、频率网格和常数，包括原有的 0.528 Å 原子偶极矩换算，分母阻尼固定为 0.05 eV（不等同于已认证的光谱半高全宽）。若出现负响应值，会保留原值并标记待核对。参考值修复本身不构成对绝对截面、前因子或态数收敛性的验证。Python 与 MATLAB 路线均用于既有计算流程的后处理。切换实现时请用已知输入交叉核对，目前未认证二者数值完全等价。有限态 SOS 求和需要检查态数收敛性；比较截面时应报告电子结构方法、基组、溶剂处理、纳入的电子态、偶极矩输入和阻尼／展宽约定，峰高尤其依赖展宽参数。不同实现之间应使用一致设置。

## 理论与软件参考文献

- **原工作流注明的直接方法参考：** F. Terenziani, C. Katan, E. Badaeva, S. Tretiak and M. Blanchard-Desce. [Enhanced Two-Photon Absorption of Organic Chromophores: Theoretical and Experimental Assessments](https://doi.org/10.1002/adma.200800402). Advanced Materials **20**, 4641–4678 (2008). DOI: `10.1002/adma.200800402`。
- **SOS 响应理论基础：** B. J. Orr and J. F. Ward. [Perturbation theory of the non-linear optical polarization of an isolated system](https://doi.org/10.1080/00268977100100481). Molecular Physics **20**, 513–526 (1971). DOI: `10.1080/00268977100100481`。
- **双光子跃迁理论奠基文献：** M. Göppert-Mayer. [Über Elementarakte mit zwei Quantensprüngen](https://doi.org/10.1002/andp.19314010303). Annalen der Physik **401**［分辑卷号 9］, 273–294 (1931). DOI: `10.1002/andp.19314010303`。
- **上游波函数分析软件：** T. Lu and F. Chen. [Multiwfn: A multifunctional wavefunction analyzer](https://doi.org/10.1002/jcc.22885). Journal of Computational Chemistry **33**, 580–592 (2012). DOI: `10.1002/jcc.22885`。使用时还应注明实际 Multiwfn 版本，并引用所用 Gaussian 版本和电子结构方法的适用文献。

- **Multiwfn 近期发展：** T. Lu. [A comprehensive electron wavefunction analysis toolbox for chemists, Multiwfn](https://doi.org/10.1063/5.0216272). Journal of Chemical Physics **161**, 082503 (2024)。按照部署版本的要求，应在正文同时引用 2012 和 2024 年两篇 Multiwfn 论文。

## 相关研究

该工具页与双光子吸收机器学习、纳米石墨烯和金属有机层的相关研究相连接；相关应用论文见[仓库说明](https://github.com/sym823808458/calculateTPAbyMATLAB)，与上述理论及上游软件文献配合引用。
