视频资料：https://www.bilibili.com/video/BV14a411C7s8

# 基本原理

![](https://s2.loli.net/2022/05/31/SJIpUxR9dZBl76k.png)

**编码**：

- 二进制编码，将数值转化为二进制串，用以求解问题。
- TSP问题，比如10个城市，某个解可以表示为[3, 2, 1, 4, 5, 7, 6, 8, 9, 0]。
- 根据不同的问题，进行不同的抽象实现。

## 基本原理—复制

![复制](https://s2.loli.net/2022/05/31/voGKn2UCqphfsdl.png)

## 基本原理—交叉

![交叉](https://s2.loli.net/2022/05/31/pg3URrobkPWstZX.png)



## 基本原理—变异

![变异](https://s2.loli.net/2022/05/31/3PHAQNhK2TomkC1.png)

# 算法实现

**复制**：按适应度大小映射为概率，进行轮盘赌法复制。

**交叉**：1和2，3和4，以一定概率决定是否交叉。若交叉，则二者选择随机一个段进行交叉。

**变异**：按照一定概率决定该个体是否变异，若变异，随机选择一个位点进行变异：按位取反。



![](https://s2.loli.net/2022/05/31/grquzNFVBcvt7UI.png)