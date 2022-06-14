# 153. 寻找旋转排序数组中的最小值

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[l] # 这是把等于合并着写了，妙得很
