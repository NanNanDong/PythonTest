# 215. 数组中的第K个最大元素
# 快排的应用

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l, r): # 快排核心方法
            pivot = 1
            while l < r:
                while l < r and nums[r] >= nums[pivot]:r -= 1
                while l < r and nums[r] <= nums[pivot]:l += 1
                nums[l], nums[r] = nums[r], nums[l]
            nums[l], nums[pivot] = nums[pivot], nums[l]
            return l
        k = len(nums) - k # 第k大 = 第 len(num)-k 小
        if k >= len(nums): return nums[-1]

        l, r = 0, len(nums)-1
        while True:
            idx = partition(l, r)
            if idx == k:
                return nums[idx]
            elif idx < k:
                l = idx + 1
            else:
                r = idx - 1