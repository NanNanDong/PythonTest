# 978. 最长湍流子数组

# 非常经典有意思的一题

# 1. 一升一降交替，很明显DP
# 维护一个上升，一个下降
# 定义 up[i] 表示以位置 i 结尾的，并且 arr[i - 1] < arr[i] 的最长湍流子数组长度
# down 同理

# 2. 双指针，左边界固定的时候，右边界是可以确定的

from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        up = [1] * n
        down = [1] * n
        res = 1

        # 可以使用滚动数组，降低空间复杂度为O(1)
        for i in range(1, n):
            if arr[i - 1] < arr[i]:
                up[i] = down[i - 1] + 1 # 交替增长
                down[i] = 1 # 当前为结尾，且下降的需要重新计算
            elif arr[i - 1] > arr[i]:
                up[i] = 1
                down[i] = up[i - 1] + 1
            else:
                up[i] = 1 # 相等的不为湍流
                down[i] = 1
            res = max(res, max(up[i], down[i])) # 取一个较大的
        
        return res

