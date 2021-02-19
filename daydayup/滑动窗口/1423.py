# 1423. 可获得的最大点数
# 转化成 连续的 n-k 的最小子数组问题

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        # 窗口大小为 n-k
        windowSize = n - k
        # 选取 n-k个作为初始值
        s = sum(cardPoints[:windowSize])

        minSum = s

        for i in range(windowSize, n):
            # 滑动窗口右移动一格，增加从右元素，减少左侧元素
            s += cardPoints[i] - cardPoints[i - windowSize] # 拿size-1理解，很明确的左边界
            minSum = min(minSum, s)
        
        return sum(cardPoints) - minSum


