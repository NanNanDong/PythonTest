# 959. 由斜杠划分区域
# 维护连通分量
# 单元格内部划分：4个区域
# 单元格外部划分：向右、向下进行合并(向左、向上/向左、向下/向右、向上 --> 即可，但向右向下合逻辑些)


from typing import List

# 并查集

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n * n + 2 * n + 2))
        self.area = 1

    def find(self, x) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        self.parent[xroot] = yroot

    def isClosed(self, x, y) -> bool:
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            self.area += 1
            return True
        else:
            return False

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        n = len(grid)
        uf = UnionFind(n)
        
        # 连接边缘
        node = n * n + 2 * n + 1
        for i in range(n + 1):
            uf.union(node, i)   # 连接上边缘
            uf.union(node, n * n + n + i)   # 连接下边缘
            uf.union(node, i * (n + 1))     # 连接左边缘
            uf.union(node, i *  (n + 1) + n)    # 连接右边缘

        # 连接斜杠
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    node1 = (n + 1) * (i + 1) + j
                    node2 = (n + 1) * i + (j + 1)
                    if not uf.isClosed(node1, node2):
                        uf.union(node1, node2)
                elif grid[i][j] == '\\':
                    node1 = (n + 1) * i + j
                    node2 = (n + 1) * (i + 1) + (j + 1)
                    if not uf.isClosed(node1, node2):
                        uf.union(node1, node2)

        return uf.area






