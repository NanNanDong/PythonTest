# 724. 寻找数组的中心索引
# 先计算出所有的和，然后从开头往后开始减

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum1, sum2 = 0, 0
        for num in nums:
            sum1 += num
        
        for i in range(0, len(nums)):
            sum2 += nums[i]
            if sum1 == sum2: return i
            sum1 = sum1 - nums[i] # 减去当前的

        return -1



            
x = Solution()
# print(x.pivotIndex([1, 7, 3, 6, 5, 6]))
# print(x.pivotIndex([1, 1]))
print(x.pivotIndex([1]))
print(x.pivotIndex([]))
print(x.pivotIndex([-1,-1,-1,-1,-1,0]))
        



