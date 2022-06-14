# 162. 寻找峰值

# 想复杂了，线性扫描，找到第一个后面比前面大大就好了，就不用考虑这么多特殊值了
# 没找到则返回最后一个

from typing import List


class Solution:
    def findPeakElement1(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                return i
        
        return n - 1

    # 二分查一查
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]: # 让比较大的逐渐靠过来
                right = mid
            else:
                left = mid + 1
        return left



x = Solution()
print(x.findPeakElement([1, 2, 3, 1]))
print(x.findPeakElement([1,2,1,3,5,6,4]))
print(x.findPeakElement([1]))
print(x.findPeakElement([1,2]))
print(x.findPeakElement([3,2]))

