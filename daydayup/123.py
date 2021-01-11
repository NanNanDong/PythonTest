# 123. 买卖股票的最佳时机 III
# 动态规划：(每天两笔，买之前必须卖掉)
# 分析状态：1.未经过任何操作；2.只进行过一次买操作；3.进行一次买和卖；4.进行一次买和卖，再买一次；4.进行两次买和卖
# 1.为0，不记录，故是4个状态，分别记为buy1,sell1,buy2,sell2
# ---> 二级动态，如果一个维度不是太多，可利用数组降低个维度

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i]) # 又剁手
            sell1 = max(sell1, buy1 + prices[i]) # 割肉，赚了上次的
            buy2 = max(buy2, sell1 - prices[i]) # 赚了，加仓
            sell2 = max(sell2, buy2 + prices[i]) # 赚了，加仓马上割肉，赚今天的
            print(sell1, ",", sell2)
        return sell2 # 本应该是max(0, sell1, sell2)，但题目特殊

    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0 # 就一天，没收益
        dp = [0, -prices[0], 0, -prices[0], 0]
                # dp[0] = 0          # 保持不买不卖
        # dp[1] = -prices[0] # 第1次 买入
        # dp[2] = 0          # 第1次 卖出
        # dp[3] = -prices[0] # 第2次 买入
        # dp[4] = 0          # 第2次 卖出
        for i in range(1, n):
            dp[1] = max(dp[1], dp[0] - prices[i])
            dp[2] = max(dp[2], dp[1] + prices[i])
            dp[3] = max(dp[3], dp[2] - prices[i])
            dp[4] = max(dp[4], dp[3] + prices[i])
        return dp[4]

x = Solution()
print(x.maxProfit([3,3,5,0,0,3,1,4]))