# 137. 只出现一次的数字 II

import collections

from typing import List

# https://leetcode-cn.com/problems/single-number-ii/solution/zhi-chu-xian-yi-ci-de-shu-zi-ii-by-leetc-23t6/

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         cache = collections.defaultdict(int)
#         for num in nums:
#             cache[num] += 1
        
#         for i in cache:
#             if cache[i] == 1:
#                 return i

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 31:
                if i == 31:
                    res -= (1 << i)
                else:
                    res |= (1 << i)
            
        return res






        
