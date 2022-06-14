# 496. 下一个更大元素 I

# 739 单调栈过来的，如果自己看，肯定觉得是排序，或者堆

# 没有重复元素，且是子集，那num2计算一遍，按照num1的返回不就行了
# https://leetcode-cn.com/problems/next-greater-element-i/solution/dan-diao-zhan-zong-jie-by-wu-xian-sen-2/
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        dic, stk = {}, []

        for i in range(n):
            while stk and nums2[i] > stk[-1]:
                dic[stk.pop()] = nums2[i]
                stk.append(nums2[i])
                
        return [dic.get(x, -1) for x in nums1] # 这个dict用的秒，还是python大法好

  



