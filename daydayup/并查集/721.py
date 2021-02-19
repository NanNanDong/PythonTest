# 721. 账户合并
# 并查集 + 哈希表
# 1. 先初始化每个账户为1个连通分量
# 2. 遍历每个账户下的邮箱，判断该邮箱是否在其他账户下出现
# 3. 如果未出现，继续
# 4. 如果账户A、B下出现了相同的邮箱email，那么将账户A和账户B两个连通分量进行合并
# 5. 最后遍历并查集中每个连通分量，将所有连通分量内部账户的邮箱全部合并(相同的去重，不同的合并)
# 6. 结束

from typing import List
import collections

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def union(self, x: int ,y: int):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY: return
        self.parent[rootX] = rootY

        # self.parent[self.find(index2)] = self.find(index1) # 分开写，好理解些
    
    def find(self, x: int) -> int:
        if self.parent[x] != x: # 把路径压缩合并进去了
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToIndex = dict()
        emailToName = dict()
        
        # 初始化每个账户为1个连通分量
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in emailToIndex:
                    emailToIndex[email] = len(emailToIndex)
                    emailToName[email] = name
        
        # 遍历每个账户下的邮箱，判断该邮箱是否在其他账户下出现
        uf = UnionFind(len(emailToIndex))
        for account in accounts:
            firstIndex = emailToIndex[account[1]]
            for email in account[2:]: # 出现则合并连通分量
                uf.union(firstIndex, emailToIndex[email])

        # 利用set去重
        indexToEmails = collections.defaultdict(list)
        for email, index in emailToIndex.items():
            index = uf.find(index)
            indexToEmails[index].append(email)
        
        # 组装最后的数据
        ans = list()
        for emails in indexToEmails.values():
            ans.append([emailToName[emails[0]]] + sorted(emails))
            # print(emailToName[emails[0]], sorted(emails))
        return ans


x = Solution()
x.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]])
