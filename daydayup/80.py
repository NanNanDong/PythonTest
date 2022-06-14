# 80. 删除有序数组中的重复项 II

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return n

        slow = fast = 2

        # while fast < n:
        #     if nums[slow - 2] != nums[fast]:
        #         nums[slow] = nums[fast]
        #         slow += 1
        #     fast += 1

        for i in range(2, n):
            if nums[slow - 2] != nums[i]:
                nums[slow] = nums[i]
                slow += 1
        
        print(nums)

        return slow

x = Solution()
# print(x.removeDuplicates([1, 1, 1, 2, 2, 3]))
print(x.removeDuplicates([1,2,3]))


