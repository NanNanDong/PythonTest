# 26. 删除有序数组中的重复项

# 原地删除，返回大小，竟然还有序
from typing import List


class Solution:
    # 双指针
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n

        size = 0 # 当前已排序的后一位

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                size += 1
                nums[size] = nums[i]
        
        return size + 1
        

x = Solution()
print(x.removeDuplicates([1, 1, 1, 2]))
print(x.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


