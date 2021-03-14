# 46. 全排列

# 回溯入门！
# 广度优先

# 深度优先，需要状态重置(回溯)：
# 状态变量：depth(递归到第几层)、path(已经选了哪些数)、used(数组存储当前是否被使用)

# https://leetcode-cn.com/problems/permutations/solution/quan-pai-lie-by-leetcode-solution-2/
# ---> 图非常形象，就是从当前level开始，后面都数字依次和当前level的位置交换，
# 然后dfs扎进去，往上回溯的时候要恢复

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def dfs(output: List[int], level = 0):
            # 所有数都填完了
            if level == n:
                res.append(output[:]) # 添加副本
            
            for i in range(level, n): 
                # 动态维护数组
                output[level], output[i] = output[i], output[level]
                # 继续递归填下一个数
                dfs(level + 1, output)
                # 撤销操作
                output[level], output[i] = output[i], output[level]

        dfs(nums)

        return res
        

        


        