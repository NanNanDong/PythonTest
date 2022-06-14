# 690. 员工的重要性

# Definition for Employee.
from typing import List

# https://leetcode-cn.com/problems/employee-importance/solution/690-yuan-gong-de-zhong-yao-xing-dfsshi-x-qvt4/

# 应该是DFS，mp存储 id和员工 的映射

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mp = {employee.id: employee for employee in employees}
        # print(mp)
        
        def dfs(idx: int) -> int:
            employee = mp[idx]
            total = employee.importance + sum(dfs(sub_idx) for sub_idx in employee.subordinates)
            return total

        return dfs(id)

x = Solution()
v = x.getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1)
print(v)
        



        


