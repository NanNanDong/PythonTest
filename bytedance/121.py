# 121. 买卖股票的最佳时机
# 1次买卖
# 贪心/动态规划
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit

    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0 # 边界条件
        dp = [0] * n
        minPrice = prices[0]

        for i in range(1, n):
            minPrice = min(minPrice, prices)
            dp[i] = max(dp[i-1], prices[i] - minPrice)
        
        return dp[-1]


x = Solution()
print(x.maxProfit([]))


