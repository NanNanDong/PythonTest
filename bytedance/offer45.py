# 剑指 Offer 45. 把数组排成最小的数

# 排序规则：就按照 x + y 和 y + x 的结果来
from typing import List


class Solution:

    # 快速排序
    def minNumber1(self, nums: List[int]) -> str:
        strs = [str(num) for num in nums]

        def quick_sort(l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1 # 右哨兵找小的
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1 # 左哨兵找大的
                strs[i], strs[j] = strs[j], strs[i]
            
            strs[i], strs[l] = strs[l], strs[i]
            quick_sort(l, i - 1)
            quick_sort(i + 1, r)

        quick_sort(0, len(strs) - 1)
        return ''.join(strs)

    # 内置排序
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b: return 1
            elif a < b: return -1
            else: return 0
        
        strs = [str(num) for num in nums]
        strs.sort(key= functools.cmp_to_key(sort_rule))
        return ''.join(strs)






