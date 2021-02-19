# 947. 移除最多的同行或同列石头
# 1. 怎么保证移除最多？交叉位置多石头不能先移除 ---> 求图多连通分量 (并查集的个数- 连通分量)， 连通分量；find()不存在则加入map，连通分量+1，union的时候对应-1
# 2. 给了坐标：提示可以用并查集，底层数组是横坐标和纵坐标
# 3. 给了横纵坐标的范围：为了避免横纵坐标在数值上相同，纵坐标+1000
# 4. 和普通并查集不太一样的是，这个数组大小由传入的二维数组决定，所以使用map动态扩容

from typing import List

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.count = 0
    
    def find(self, x: int):
        if x not in self.parent:
            self.parent[x] = x
            self.count += 1 # 并查集集中新加入一个结点，结点的父亲结点是它自己，所以连通分量的总数 +1
            print(self.count, x)
        
        if x != self.parent[x]: # 路径压缩：如果不是根节点，则把它指向其父节点的父节点
            self.parent[x] = self.find(self.parent[x]) 
            return self.parent[x]
        
        return x

    def union(self, x: int, y: int):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY: return

        self.parent[rootX] = rootY
        # 两个连通分量合并成为一个，连通分量的总数 -1
        self.count -= 1


class UF:
    def __init__(self, M):
        self.parent = {}
        self.cnt = 0

    def find(self, x):
        if x not in self.parent:
            self.cnt += 1
            self.parent[x] = x
            print(self.cnt, x)
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return x
    def union(self, p, q):
        if self.connected(p, q): return
        leader_p = self.find(p)
        leader_q = self.find(q)
        self.parent[leader_p] = leader_q
        self.cnt -= 1
    def connected(self, p, q):
        return self.find(p) == self.find(q)
        
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        unionFind = UnionFind()
        for stone in stones:
            unionFind.union(~stone[0], stone[1])
        return len(stones) - unionFind.count


    def removeStones1(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UF(0)
        for i in range(n):
            uf.union(stones[i][0] + 10001, stones[i][1])
        return n - uf.cnt


x = Solution()
# print(x.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
print(x.removeStones([[0,1],[1,0]]))
# print(x.removeStones1([[0,1],[1,0]]))

