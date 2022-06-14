# 977. 有序数组的平方

# https://leetcode-cn.com/problems/squares-of-a-sorted-array/solution/shuang-zhi-zhen-jian-dan-yi-dong-by-zht-11/


from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            nums[i] = nums[i] * nums[i]
            
        nums.sort()
        return nums

    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
  

    
x = Solution()
print(x.sortedSquares([-7,-3,2,3,11]))
