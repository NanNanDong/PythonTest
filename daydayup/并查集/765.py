# 
# 演变：交换之后的连通分量个数-交换之前的连通分量个数=最少交换次数
# 交换之后，即为n/2

from typing import List

class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
            

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY: 
            if rootY < rootY:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
            self.count -= 1
        

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        size = len(row)
        n = size // 2
        uf = UnionFind(n)

        i = 0
        while i < size:
            uf.union(row[i] // 2, row[i + 1] // 2) # 基于整除向下取整, python强制允许强转，需要//
            i += 2

        return n - uf.count

x = Solution()
print(x.minSwapsCouples([0, 2, 1, 3]))

