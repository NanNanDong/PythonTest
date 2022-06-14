# 518. 零钱兑换 II

# 和39题，组合总和 比较

# 本质可理解为跳楼梯的思想，比如硬币面额为(1,2,5)，相当于可以跳1,2,5阶，然后求跳到第amount阶的组合数
# dp[i] = dp[i-1] + dp[i-2] + dp[i-5];

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        
        return dp[amount]