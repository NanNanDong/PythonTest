# 739. 每日温度

from typing import List


class Solution:
    def dailyTemperatures1(self, T: List[int]) -> List[int]:
        n = len(T)
        if n <= 1: return [0]
        diff, max = 0, 10**9

        res = []
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                if T[j] > T[i]:
                    res.append(j - i)
                    break
                
                if j == n - 1:
                    res.append(0)

        res.append(0)

        return res

    # 单调不增的栈，放index
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        res = [0] * n

        stk = []

        for i in range(n):
            nxt = T[i]
            # 当前元素比单调不增的栈顶大，则可出栈
            while stk and nxt > T[stk[-1]]: # while是因为这个丢进去，可能能弹出好几个
                idx = stk.pop()
                res[idx] = i - idx
            stk.append(i) # 栈内压入index
            
        return res
            


    

x = Solution()
print(x.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
                


