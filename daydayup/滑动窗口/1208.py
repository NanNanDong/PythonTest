# 1. 可以直接生成一个数组 record， record[i] 就表示把 s[i] 和 t[i] 转化成相等的 cost
# 2. 问题就转化为：在一个数组中，在连续子数组的和小于等于 maxCost 的情况下，找到最长的连续子数组长度
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        record = []
        for i in range(n):
            record.append(abs(ord(t[i]) - ord(s[i])))
        
        start, end = 0, 0
        windowsum = 0
        res = 0

        for end in range(n):
            windowsum += record[end]

            if windowsum > maxCost: # 滑不动了，左移
                windowsum -= record[start]
                start += 1

        # res = max(res, end - start + 1) # 可能没啥必要
        return n - start

    def equalSubstring1(self, s: str, t: str, maxCost: int) -> int:
        # 求连续子数组的 sum, 且 sum <= maxCost, 找子数组的最大长度
        # 使用滑动窗口求解即可
        n = len(s)
        start = end = sumCost = 0
        for end in range(n):
            sumCost += abs((ord(s[end]) - ord(t[end])))
            if sumCost > maxCost:
                sumCost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
        
        return n - start

