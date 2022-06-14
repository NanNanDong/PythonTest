# 90. 子集 II

# 一般情况下，看到题目要求「所有可能的结果」，而不是「结果的个数」，我们就知道需要暴力搜索所有的可行解了，可以用「回溯法」。
# 回溯法是一种算法思想，而递归是一种编程方法，回溯法可以用递归来实现。

# 

from typing import List


class Solution:
    # 排序后暴力搜索
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        cur = []
        
        def dfs(nums, u, cur, res):
            # 所有位置都决策完成
            if u == len(nums):
                res.add(tuple(cur))
                return
            
            # 选择当前位置的元素，往下决策
            cur.append(nums[u]) 
            dfs(nums, u + 1, cur, res)

            # 不选当前位置的元素（回溯），往下决策
            cur.pop()
            dfs(nums, u + 1, cur, res)

        dfs(nums, 0, cur, res)
        
        return [list(x) for x in res]


        

        