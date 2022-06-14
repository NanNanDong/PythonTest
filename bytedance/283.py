# 283. 移动零

# 高级点，双指针思想
# 左指针左边均为非零数
# 右指针左边直到左指针处均为零

from typing import List


class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        zeroIdx = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                zeroIdx = i
                break

        for i in range(zeroIdx, n):
            if nums[i] != 0:
                nums[zeroIdx], nums[i] = nums[i], nums[zeroIdx]
                zeroIdx += 1

        # print(nums)

    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left, right = 0, 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left] # 如果没遇到0相当于原地换
                left += 1
            right += 1
        
        print(nums)

    

x = Solution()
# x.moveZeroes([0, 1, 0, 3, 12])
x.moveZeroes([7, 1, 0, 3, 12])


