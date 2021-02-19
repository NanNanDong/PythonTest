# 674. 最长连续递增序列
# 求的是连续的，所以不用dp/二分替换

from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        numsLen = len(nums)
        if numsLen == 0: return 0

        lisLen, curLen = 1, 0
        
        for i in range(0, numsLen):
            if nums[i] > nums[i-1]:
                curLen += 1
            else:
                lisLen = max(lisLen, curLen)
                curLen = 1
        
        return max(lisLen, curLen)

x = Solution()
print(x.findLengthOfLCIS([1,3,5,4,7]))
print(x.findLengthOfLCIS([2,2,2,2,2]))
print(x.findLengthOfLCIS([2]))
print(x.findLengthOfLCIS([1,3,5,7]))
          

            

