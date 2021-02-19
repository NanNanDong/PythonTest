# 665. 非递减数列
# 注意虽然是easy题，但是需要考虑替换后，要赋值进行比较
from typing import List
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        size = len(nums)
        if size == 1: return True
        k = 1
        for i in range(1, size):
            if nums[i-1] > nums[i]:
                k -= 1
                if i == 1 or nums[i] >= nums[i - 2]: # 第一个 & 优先往小调
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1] # 不成了，那就往临近的一个调，不然像 3，4，2，5的成3，4，3，5也不成的
                if k < 0:
                    return False
            
        return True

x = Solution()
print(x.checkPossibility([4,2,3]))
# print(x.checkPossibility([4,2,1]))
print(x.checkPossibility([3,4,2,3]))

