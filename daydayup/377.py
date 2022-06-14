# 377. 组合总和 Ⅳ

# 1.初始化dp[0]=1
# 2.遍历i从1到target，
#   对于每个i：遍历nums中到每个元素num，当num<=i，将dp[i-num]的值加到dp[i]
# 3.dp[target]即为答案

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]

        return dp[target]



