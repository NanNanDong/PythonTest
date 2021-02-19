# 561. 数组拆分 I

# 晃眼一看，不就是个排序？但返回的是最大的和
# 还是排序，因为最大的一定会被浪费，此题是贪心，第二大的保留

from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        arrs = sorted(nums)
        return sum(arrs[::2])


x = Solution()
print(x.arrayPairSum([1, 4, 3, 2]))
print(x.arrayPairSum([6,2,6,5,1,2]))