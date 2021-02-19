# 485. 最大连续1的个数
from typing import List

class Solution:
    def findMaxConsecutiveOnes1(self, nums: List[int]) -> int:
        isValid = False
        left = -1
        size = len(nums)
        maxx = 0
        for i in range(size):
            if nums[i] == 1:
                if not isValid: # 后置处理最后位为1
                    left = i
                    isValid = True                    
            else:
                if isValid:
                    lenx = i - left
                    maxx = max(maxx, lenx)
                    isValid = False

        if nums[size - 1] == 1:
            return max(maxx, size - left)
        
        return maxx
    
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = count = 0
        for i, num in enumerate(nums):
            if num == 1:
                count += 1 # 不断更新count
            else:
                maxCount = max(maxCount, count) # 巧妙的在计算max后，将count赋为0，避免出现1后面很多0的问题
                count = 0
        maxCount = max(maxCount, count)
        return maxCount

x = Solution()
print(x.findMaxConsecutiveOnes([1,1,0,1,1,1]))     
print(x.findMaxConsecutiveOnes([0,0,0,1]))
print(x.findMaxConsecutiveOnes([0]))
print(x.findMaxConsecutiveOnes([1]))

            


            
