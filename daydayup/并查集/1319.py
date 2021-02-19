# 1319. 连通网络的操作次数
# 1. 存在n个计算机，所以最开始建立n个连通分量，每个网络计算机是一个连通分量
# 遍历Connections数组，将相应的网络计算机（连通分量）合并成同一个网络
# 2. 合并时，作以下判断：
# 如果两个连通分量不同源（根节点不相同），合并；
# 如果两个连通分量同源（根节点相同），说明该连接多余，则将多余的连接线数量+1
# 3. 最后可以计算得出网络中要多少个连通分量，假设有n个。要将n个连通分量连接到一起，至少需要n-1根多余的网络连接线

# 初始情况下有n个点的图现有m个连通变量，那么想要整张图连通，两个连通变量间都需要一条边来连接，
# 所以m个连通变量就需要m-1个边，最少移动的边的个数也就m-1个。当然边的总数不能小于n-1条，否则数量就不够了

from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前的连通分量数目
        self.setCount = n

    
    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y: return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def isConnected(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        return x == y

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1

        uf = UnionFind(n)
        for x, y in connections:
            uf.union(x, y)

        return uf.setCount - 1






