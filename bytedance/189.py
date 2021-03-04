# 189.旋转数组
# 尽可能相处三种以上的方案，O(1)的空间复杂度

# 1. 瞬间想到的就是O(1)，找数字交换的规律
# 2. 也是O(1)，先整个交换，再交换前半部分，后交换后半部分  --> 环状替换

from typing import List


class Solution:
    # def rotate1(self, nums: List[int], k: int) -> None:
    #     n = len(nums)
    #     k %= n

    #     nums[0:n] = reversed(nums[0:n])
    #     nums[0:k] = reversed(nums[0:k])
    #     nums[k:n] = reversed(nums[k:n])


x = Solution()
print(x.rotate([1,2,3,4,5,6,7], 3))
