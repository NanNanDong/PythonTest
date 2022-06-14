# 75. 颜色分类

# 多路快排？没那么复杂，维护两个index即可，一个从左一个从右边
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:

        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        n = len(nums)

        if n < 2: return
        pos1, pos2, i = 0, n - 1, 0

        while i <= pos2:
            if nums[i] == 0:
                swap(nums, i, pos1)
                i += 1
                pos1 += 1
            elif nums[i] == 1:
                i += 1
            else:
                swap(nums, i, pos2)
                pos2 -= 1




