# 42. 接雨水

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length < 3: return 0
        res, idx = 0, 0
        stack = []
        while idx < length:
            while len(stack) > 0 and height[idx] > height[stack[-1]]: 
                # 计算宽度的时候，是当前的下一个，所以要pop，后面利用木桶效应，计算一条的水量 --> 画个图很清楚
                top = stack.pop()
                # print('top -> ', top)
                if len(stack) == 0: break
                h = min(height[stack[-1]], height[idx]) - height[top] # 木桶效应，要比较
                dist = idx - stack[-1] - 1
                res += (dist * h)
            stack.append(idx) # 维护单调递减，后面符合条件马上pop掉了
            # print('push ->', idx)
            # print('stack is ->', stack)
            idx += 1
        return res

x = Solution()
print(x.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print('---------')
print(x.trap([4,2,0,3,2,5]))
