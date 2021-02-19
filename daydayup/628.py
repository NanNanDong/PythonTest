# 628. 三个数的最大乘积
# 1. 排序后，比较最大3个数的乘积 和 最大的数*最小两个数
# 2. 线性的去查找
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-1] * nums[-2] * nums[-3]
        b = nums[0] * nums[1] * nums[-1]
        return max(a, b)

    def maximumProduct1(self, nums: List[int]) -> int:
        a = b = c = float('-inf') # 较大的
        d = e = float('inf')
        for i, num in enumerate(nums):
            # 更新较大的
            if num > a :
                a, b, c = num, a, b
            elif num > b:
                b, c = num, b
            elif num > c:
                c = num
            # 更新较小的
            if num < d:
                d, e = num, d
            elif num < e:
                e = num
            
        return max(d * e * a, a * b * c)
            
