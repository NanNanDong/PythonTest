# 1438. 绝对差不超过限制的最长连续子数组
# python2用有序集合，不然得维护max和min
# python3得利用两个deque模拟

from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left, right, res = 0, 0, 0
        minq = deque()
        maxq = deque()

        for num in nums:
            # 当前数字是最大最小时，更新队列
            while len(minq) and num < minq[-1]: minq.pop()
            while len(maxq) and num > maxq[-1]: maxq.pop()
            minq.append(num)
            maxq.append(num)
            right += 1

            while maxq[0] - minq[0] > limit:
                # 只会进入其中一条
                if minq[0] == nums[left]: minq.popleft()
                if maxq[0] == nums[left]: maxq.popleft()
                left += 1
            
            res = max(res, right - left)

        return res




    
    # def longestSubarray(self, nums, limit):
    #     from sortedcontainers import SortedList
    #     s = SortedList() # python2才支持
    #     n = len(nums)
    #     left, right, res = 0, 0, 0
    #     while right < n:
    #         s.add(nums[right])
    #         while s[-1] - s[0] > limit: # 最大减去最小
    #             s.remove(nums[left])
    #             left += 1
    #         res = max(res, right - left + 1)
    #         right += 1

    #     return res



x = Solution()
print(x.longestSubarray([8,2,4,7]))
print(x.longestSubarray([10,1,2,4,7,2]))
print(x.longestSubarray([4,2,2,2,4,4,2,2]))
