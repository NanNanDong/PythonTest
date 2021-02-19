# 34. 在排序数组中查找元素的第一个和最后一个位置
# 看题目意思，肯定要二分了，分情况考虑(坑点是中位数都取法)
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/zai-pai-xu-shu-zu-zhong-cha-zhao-yuan-su-de-di-3-4/
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/yi-wen-dai-ni-gao-ding-er-fen-cha-zhao-j-ymwl/
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        if size == 0: return [-1, -1]
        
        first_pos = self.find_first_pos(nums, size, target)
        if first_pos == -1: return [-1, -1]
        last_pos = self.find_last_pos(nums, size, target)
        return [first_pos, last_pos]

    
    def find_first_pos(self, nums: List[int], size: int, target:int) -> int:
        left = 0
        right = size - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid
            else:
                right = mid - 1
        if nums[left] == target:
            return left
        else:
            return -1
        
    def find_last_pos(self, nums: List[int], size: int, target:int) -> int:
        left = 0
        right = size - 1
        while left < right:
            mid = left + (right - left + 1) // 2 # 注意：中位数，上取整
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left = mid
            else:
                left = mid + 1
        # 由于能走到这里，说明在数组中一定找得到目标元素，因此这里不用再做一次判断
        return left

x = Solution()
print(x.searchRange([5,7,7,8,8,10], 8))