# 778. 水位上升的泳池中游泳
# 1. 并查集+计数排序
# 模拟下雨过程，就考虑此时和雨水高度相等的单元格，不断添加到集合中
# 每次检查左上和右下是否相连
# 2. Dijkstra：没有负权边的最短路径问题

from typing import List
import collections

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    # 私有操作
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x]) # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n = len(grid)

        # 因为需要从小到大考虑时刻 t，从平台高度 t 出发判断是否能与相邻的方块连通
        # 所以这里需要存储每个平台高度对应的位置
        idx = [0] * (n * n)
        for i in range(n):
            for j in range(n):
                idx[grid[i][j]] = (i, j)

        # print(idx)
        uf = UnionFind(n * n)
        for t in range(n * n):
            # 对高度为 t 的平台进行判断是否能与相邻四个方位的平台连通
            x, y = idx[t]
            for dx, dy in directs:
                nx = x + dx
                ny = y + dy
                # 当前坐标在区域内 且 该点可达
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] <= t:
                    # 尝试合并相邻的平台
                    uf.union(x * n + y, nx * n + ny)

            # 检查左下角与右下角是否连通
            if uf.isConnected(0, n * n - 1): return t
        
        return -1


x = Solution()
print(x.swimInWater([[0,2],[1,3]]))