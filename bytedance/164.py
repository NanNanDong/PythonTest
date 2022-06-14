# 164. 最大间距

# 为啥是困难？
# 原来目的是要用O(N)时间复杂度的
# 基数排序、桶排序

# https://leetcode-cn.com/problems/maximum-gap/solution/tong-pai-xu-by-powcai/

from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        orderedNum = sorted(nums)
        res = 0
        n = len(orderedNum)
        if n <= 1:
            return res

        # print(orderedNum)

        for i in range(1, n):
            pre = orderedNum[i - 1]
            cur = orderedNum[i]
            res = max(cur - pre, res)

        return res

x = Solution()
print(x.maximumGap([3, 6, 9, 1]))