# 122. 买卖股票的最佳时机 II

# 很简单的单调增的都取出来

# dp[i][0]=max{dp[i−1][0],dp[i−1][1]+prices[i]}
# dp[i][1]=max{dp[i−1][1],dp[i−1][0]−prices[i]}

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0

        cur_min = prices[0]

        res = 0
        for i in range(1, n):
            if prices[i] >= cur_min:
                res += (prices[i] - cur_min)

            cur_min = prices[i]
        return res

x = Solution()
print(x.maxProfit([1,2,3,4,5]))
# print(x.maxProfit([7,1,5,3,6,4]))




