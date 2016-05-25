# coding=utf-8
'''
Created on 2016年5月25日
@author: a1

数理统计与参数估计（与概率论不同，数理统计往往做的是参数估计）
统计量：
    期望方差、偏度、峰度
    协方差、相关系数
    独立不相关
1. 事件的独立性
    P(AB) = P(A)P(B),则称事件A和B相互独立。
    实践中判断独立性：依据实际两个事件是否相互影响。
    如果A，B相互独立，A，B相互包含的信息量为0.
2. 期望
    离散型：加权和
    连续型：积分
    若X/Y相互独立：E(XY) = E(X)E(Y)
    反之不成立。实际上，若E(XY) = E(X)E(Y)，只能表明X/Y不相关。
    例1：异或...利用二进制
    例2：集合Hash问题
    将任意字符串非均匀映射到正整数k，概率为2^-k。现有字符串集合S，经元素映射后，得到
    的最大整数位10，求集合S
3. 方差：
    Var(X = E{[X - E(X)]^2} = E(X^2) - E^2(X)
    Var(kX) = k^2Var(X)
    如果X、Y独立，Var(X + Y) = Var(X) + Var(Y)
4. 协方差
    Cov(X,Y) = E(XY) - E(X)E(Y)
    由此可以做一个定义：若其为0，表示XY不相关。
    协方差>0, 他们的变化趋势相同；
    协方差<0, 他们的变化趋势相反
    协方差=0, 称X和Y不相关（圆形）
    Cov(X,Y) <= 两者方差之积，当其关系为线性时，相关系数为1.（协方差有上界而已，不一定为1）
5. 不相关和独立：独立指XY概率为两者边缘概率乘积。不相关指示说协方差为0.
    理解？感觉独立是说概念上的两者是否有关系。相关性只是从数据来看变化趋势是否有相同关系。
    
    若X与Y不相关，说明X与Y之间没有线性关系，但是可能有其它函数关系。（即不能保证两者独立）
6. Pearson相关系数：
    因为Cov(X,Y) <= 两者方差之积.
    相关系数 = Cov(X,Y) / 根号(两者方差之积)    <= 1
    可以看出来：相关系数，可以说是标准化后的协方差！
7. 协方差矩阵
    对于n各随即向量，我们计算任意两个向量之间的协方差，得到协方差矩阵。
8. 矩
    k阶原点矩：E(X^k)    1阶原点矩就是期望
    k阶中心距：E{[E-E(X)]^k}    2阶中心距就是方差
9. 统计参数：
    期望
    方差
    变异系数：方差/期望，分布离散程度
    偏度（三阶）：衡量随机变量概率分布的不对称性
    峰度（四阶）：高低（正态分布的峰度定义为0，正态分布按照算式计算结果正好为3，最后-3变为0）
10. 切比雪夫不等式：
    设随机变量X的期望为u,方差为..,对于任意正数，试估计概率P{|X-u|<e}的下限？
    即：随机变量的变化值落在期望值附近的概率？
    切比雪夫不等式：（使用积分来近似计算）
        P{|X-u|>=e} <= 方差/e^2
    说明：X的方差越小，上述事件发生的概率越大。即：X的取值基本上集中在期望附近。
        该不等式进一步说明了方差的含义；
        该不等式可证明大数定理（n很大时，加和平均 接近等于 期望）。（加和平均计算时的概率是1/n）
    重要推论：
        相当于是频率无限会接近概率。（概率论的理论基础）
11. 中心极限定理：
    多个独立变量的加和，接近正态分布。（后用来证明线性回归中的最小二乘法）
12. 样本统计量：
    样本均值
    样本方差
    注意：样本方差分母使用n-1，是为了无偏。（证明？）
13. 样本的矩（较简单，为了比较最大似然估计）
    k阶矩：...
    类似随机变量的矩。
    假定n个抽样独立同分布，可以通过n各样本方便计算样本的k阶矩。
    假设样本的k阶矩等于总体的k阶矩，从而估计出总体的参数。
        （k阶矩是参数的一个函数，令k分别等于1、2、3、4，由参数的个数决定，几个参数我得到几个式子）
    这就是著名的矩估计。
    
    矩估计的结论：（根据各自的中心距相等，我们可以计算参数中的各个未知量）
    正态分布的矩估计：使用样本期望、方差来估计整体期望、方差。
    均匀分布的矩估计：由样本来估计上下界。
14. 贝叶斯公式带来的思考
    给定某些样本D，在这些样本中计算某结论A1、A2...An出现的概率，即P(Ai|D)
    （利用已知样本，反推最有可能导致这样结果的参数值）
15. 最大似然估计：（绝对重点）即找出与样本的分布最接近的概率模型
    设总体分布为...
    抽样样本X1,X2...Xn，因为X独立同分布
    参数取多少，可以使得我们的似然函数（在已知样本的情况下）取值（各个样本取值概率乘积）最大。
    
    问题转变：如何找到这么一个结果？（求最大值，极值，一般求导数）
    具体实践操作：
        但是相乘求导使得式子变得更加复杂。我们两边取log！！！之后使得求导变成累加，简化式子
16. 二项分布的最大似然估计
    实际例子：
        10次抛硬币的结果是：正正反正正正反反正正
        我们要估计每次抛硬币结果为正的概率： p^7*(1-p)^3 = P
        那么什么时候这个P会取得最大值？ 求导找到最大值时，p=0.7
    这个0.7其实就是频率。
17. 正态分布的最大似然估计：
    已知其服从高斯分布，去求参数。
    
    ！！因此引出了最大似然估计的缺点：
    （1）需要事先假设数据分布？正态还是？
    （2）其求导为0计算的可能是局部最优值？
18. 最大似然估计与过拟合：
    二项分布：可以分子+5，分母+10

补充：最大似然估计 与 最小二乘法
    看似最小二乘估计与最大似然估计在推导得到的结果很相似，但是其前提条件必须引起大家的注意！！！
    （1）对于最小二乘估计，最合理的参数估计量应该使得模型能最好地拟合样本数据，也就是估计值和观测值之差的平方和最小，
    （2）最大似然法，最合理的参数估计量应该使得从模型中抽取该n组样本观测值的概率最大，也就是概率分布函数或者说是似然函数最大。
    显然，这是从不同原理出发的两种参数估计方法。因此最大似然法需要已知这个概率分布函数，一般假设其满足正态分布函数的特性，
在这种情况下，最大似然估计和最小二乘估计是等价的，也就是说估计结果是相同的，但是原理和出发点完全不同。
    最小二乘法以估计值与观测值的差的平方和作为损失函数，极大似然法则是以最大化目标值的似然概率函数为目标函数，
从概率统计的角度处理线性回归并在似然概率函数为高斯函数的假设下同最小二乘建立了的联系。
'''






