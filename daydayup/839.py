
# 并查集 + 判读两个字符串是否相似

from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.regions = n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX == parentY:
            return
        
        self.parent[parentX] = parentY
        self.regions -= 1

    def getRegions(self) -> int:
        return self.regions


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(str1: int, str2: int):
            count = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    count += 1
            return count == 2 or count == 0


        n = len(strs)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if isSimilar(strs[i], strs[j]):
                    uf.union(i, j)
        return uf.getRegions()

