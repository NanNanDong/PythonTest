# 1584. 连接所有点的最小费用
# 从题目意思上能读出一点 边 为权的并查集
# Kruskal 算法:常见并且好写的最小生成树算法，该算法的基本思想是从小到大加入边，是一个贪心算法。
# 其算法流程为：
# 1. 将图 G={V,E} 中的所有边按照长度由小到大进行排序，等长的边可以按任意顺序。
# 2. 初始化图 G' 为 {V,∅}，从前向后扫描排序后的边，如果扫描到的边 e 在 G' 中连接了两个相异的连通块,则将它插入 G'中。
# 3. 最后得到的图 G'就是图 G 的最小生成树。

from typing import List
class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))
    
    def find(self, x: int) -> int:
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]
    
    def unionSet(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False

        if self.rank[fx] < self.rank[fy]: # 基于rank的压缩
            fx, fy = fy, fx
        
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])

        n = len(points)
        dsu = DisjointSetUnion(n)
        edges = list()

        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(i, j), i, j))
        
        edges.sort()
        
        ret, num = 0, 1
        for length, x, y in edges:
            if dsu.unionSet(x, y):
                ret += length
                num += 1
                if num == n:
                    break
        
        return ret
