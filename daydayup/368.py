# 368. 最大整除子集

# 先排序
# dp[i]：对i来说最长的数组

# https://leetcode-cn.com/problems/largest-divisible-subset/solution/dong-tai-gui-hua-python-by-tangentc-j50f/
# --> 画表后，需要排序后，记录dp[i]，倒序查找

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = dict()

        res = []

        for num in nums:
            max_list = []
            for key, val in dp.items(): # dp记录表
                if num % key == 0 and len(val) > len(max_list):
                    max_list = val
            if not max_list:
                dp[num] = [num]
            else:
                dp[num] = max_list + [num]
            if len(dp[num]) > len(res): # 及时更新结果值
                res = dp[num]

        return res

