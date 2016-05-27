# coding=utf-8
'''
Created on 2016年5月27日
@author: a1

矩阵和线性代数

矩阵：
1. SVD：奇异值分解
    是一种重要的矩阵分解方法，可以看做对称方阵在任意矩阵的推广。
    A = U*X*V    （对于任意矩阵）
    其中U和V是正交阵[m*m和n*n]，X是奇异值,是m*n的对角矩阵
        - 正交阵：矩阵的转置*矩阵 = 单位阵
    
    有什么样好的事情发生呢？
    [u1,u2...um]*[]*[v1/v2/.../vn]
    取X的前k个（X是从大到小排列的），用来大致地获取原数据的
    - (2000*2000维度的照片，取前100维基本上已经可以看得比较清楚照片了，压缩空间)
    - (2000->100)^2倍的压缩

线性代数
2. 方阵的行列式
    主对角线的乘积和 - 副对角线的乘积和
    行列式不为0，则存在矩阵的逆。
3. 代数余子式
    去掉i行j列的数据剩下的矩阵，称为代数余子式Aij
4. 伴随矩阵
    每个位置的代数余子式形成的矩阵
5. 矩阵的逆
    A*A的伴随矩阵 = |A|*I
    - I是单位对角矩阵
6. 范德蒙行列式
    x1 != x2可以用一阶方程拟合
    x1 != x2 != x3 可以用二阶方程拟合
    x1 != x2 != ... xn 可以用n-1阶方程拟合
    这些曲线会经过每一个点。
    
    系数存在且唯一，等于 A = X的逆 * Y
7. 矩阵模型：
    考虑某随机过程T，状态有n个，用1~n表示。
    当前时刻t位于i状态，他在t+1时刻位于状态j的概率为P(i,j) = P(j|i)
        - 即状态转移的概率只依赖于前一个状态
    
    举例：人群分为上、中、下三个阶层，用1，2，3表示。
        假定当前处于某个阶层只和上一代有关。
        P为 [0.65 0.28 0.07] = 1
            [0.15 0.67 0.18] = 1
            [0.12 0.36 0.52] = 1
        这个矩阵的无穷次方会收敛！！！！
    
    概率转移矩阵：（全概率公式）
        第n+1代中处于第j个阶层的概率为：第n代处于各个阶层，下一代处于第j个阶层的概率加和
        
    若初始某一个人为各个阶层的概率为： [0.1 0.2 0.7]
        那么其下一代是各个阶层的概率为[0.1 0.2 0.7] * P
        ...
        到第n代时，会依据P转移概率矩阵慢慢收敛...[0.1 0.2 0.7] * p^n
    我们发现初始概率对最后收敛结果没有影响
    那么最后的结果一定与矩阵P的某些性质特征有关系！
8. 其实就是矩阵P最大的一个特征向量[n*n的矩阵有n个特征向量，有n个特征值]
    这是因为矩阵P的每一行和为1！！！
9. 思考
    （1）C = A*B，如何设计算法，加快矩阵运算
    （2）A*B*C / A*(B*C)
        对于一系列矩阵相乘，如何添加括号，使得计算次数最小（一个经典的动态规划问题）
10. 矩阵和向量的乘法
- 后面没有特殊说明的向量都是列向量
    A是m*n的向量，x为n*1的列向量，则A*x为m*1的列向量。
    x我们认为是n维空间的一个点。上式其实给出了一个从n维空间到m维空间点的线性变换！！！
        - 这个变换可以理解为旋转、平移
    特殊的，m=n，则是n维空间内的一个线性变换
    应用：三维空间变换、机械手臂
11. 矩阵的秩
    取出k*k的子矩阵，找到最大的可逆的子矩阵。
    则矩阵的秩就是k。
    可逆矩阵是满秩矩阵
12. 秩与线性方程组的解的关系
    A*x = b
    无解。。。
    唯一解。。。
    无穷多解。。。
13. 向量组等价
14. 系数矩阵
    C = A*B
    其中B就是系数矩阵而已。
    
特征向量
15. 正交阵
    若： A的转置*A = I 单位对角矩阵
    - A的列向量都是单位向量，且互相两两正交。[单位矩阵，乘积和为0]
    - 正交变换不改变向量长度。A*x
16. 特征值和特征向量
    lx = Ax
    含义：向量x经过矩阵A的变换，仅仅是长度发生了变化，方向上没有变化。
        我们把这样的x叫做A的特征向量，l叫做特征值。
    
    特征值的性质：
        若矩阵A存在某个特征向量 = 0，则矩阵A不可逆。因为|A|=0
17. 不同特征值对应的特征向量
    各个特征值各不相等，则各个特征值线性无关。
    - 不同特征值对应的特征向量线性无关
        - 矩阵A是对称阵时，那么各个向量不仅线性无关、还正交。
18. 白化/漂白
    任何一个矩阵A，A的转置*A一定是一个对称阵。
    用特征值和特征向量，将一个矩阵A，改成一个正交阵。- 俗称漂白
    - 会用在ICA，独立成分分析，n阶独立（麦克风声音的解耦）
    - PCA，主成分分析，只是n阶独立
        n*n的矩阵，降维成n*k的矩阵；只能保证k个矩阵正交。
        ICA能保证这些每一个向量都相互独立！ 这是两者区别
    去均值ICA分离
19. 正定阵：
    对于n阶阵A，若任意n阶向量x，都有xT*A*x > 0，则称A是正定阵。
    为什么这么定义？
        将A当做1维的，那么结论就是A为正数；
        A变成矩阵，其实就是一个n阶的推广。
    凸函数：任意两点连线都在曲线上方。
    例如：
        Z = x^2 + y^2 - xy + 8
        关于x/y求偏导，如果二阶导的矩阵是正定的，那么该曲线是凸函数。
20. 向量的导数：
    y = A*x
    求偏导的结果是一个矩阵，矩阵值为A的转置。
    线性回归中会用。
21. 标量对向量的导数
22. QR分解（没有SVD分解重要）
    利用QR分解，可以获得矩阵的特征值。
    最后An只有对角线上有值。（不断迭代）
    QR分解的求解方法有多重：Schmidt正交化、Givens变换...等


'''

