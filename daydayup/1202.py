# 1202. 交换字符串中的元素
# 读懂题目：pairs是允许交换的序列、目的是得到按字典序的最小串 --> 感觉又是并查集，毕竟一看就知道是连通性问题
# 利用并查集维护任意两点的连通性，将同属一个连通块内的点提取出来，直接排序后放置回其在字符串中的原位置即可。

from typing import List
import collections

class UnionSet:
    def __init__(self, n: int):
        self.n = n
        self.rank  = [1] * n # 表示有多少个和他相通
        self.f = list(range(n))
    
    def find(self, x: int) -> int:
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x]) # 边查变压缩
        return self.f[x]
    
    def union(self, x: int, y: int):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]: # 这里细节的
            fx, fy = fy, fx
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        unionSet = UnionSet(len(s))
        for x, y in pairs:
            unionSet.union(x, y)

        # print(unionSet)
        
        mp = collections.defaultdict(list)
        for i, ch in enumerate(s):
            mp[unionSet.find(i)].append(ch) # 根据连通 分组组成map
        
        for vec in mp.values():
            vec.sort(reverse=True) # 连通的部分排个序
        
        res = list()
        for i in range(len(s)):
            x = unionSet.find(i)
            res.append(mp[x][-1])
            mp[x].pop()

        return "".join(res)

x = Solution()
# print(x.smallestStringWithSwaps("dcab", [[0,3],[1,2]]))
# print(x.smallestStringWithSwaps("cba", [[0,1],[1,2]]))
print(x.smallestStringWithSwaps("cbadfe", [[0,1],[1,2]]))