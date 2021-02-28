# 1052. 爱生气的书店老板

# 原先就不生气的加入进来先
# 我们使用「秘密技巧」的原则是：寻找一个时间长度为 X 的窗口，能留住更多的原本因为老板生气而被赶走顾客

from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        sum = 0
        # 不生气的时间，顾客数
        for i in range(n):
            if grumpy[i] == 0:
                sum += customers[i]

        # 计算开头这一截的情况
        curValue = 0
        for i in range(X):
            if grumpy[i] == 1:
                curValue += customers[i]

        res = curValue    
        # 移动窗口，右边进入是生气的加入，左边离开生气的减掉
        for i in range(X, n):
            if grumpy[i] == 1:
                curValue += customers[i]
            if grumpy[i - X] == 1:
                curValue -= customers[i - X]
            # 取较大的
            res = max(res, curValue)

        return res + sum
