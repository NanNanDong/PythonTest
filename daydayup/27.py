# 27. 移除元素

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)

        pos = 0

        for i in range(n):
            if nums[i] != val:
                nums[pos] = nums[i]
                pos += 1
        
        return pos

x = Solution()
print(x.removeElement([3,2,2,3], 3))
print(x.removeElement([0,1,2,2,3,0,4,2], 2))



