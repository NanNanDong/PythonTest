# 136. 只出现一次的数字
# 快排
# 1. 使用集合存储数字，没有存入，有删除
# 2. 使用哈希表
# 3. 集合存储所有元素，然后 *2，减去原来的和，剩下的就是那个数
# 4. 异或大法：和0为本身、和本身为0、符合结合律和交换律

from typing import List


class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single

    def singleNumber(self, nums: List[int]) -> int:
        single = nums[0]
        for i in range(1, len(nums)):
            single ^= nums[i]
        return single

x = Solution()
print(x.singleNumber([2, 2, 1]))
print(x.singleNumber([4,1,2,1,2]))

