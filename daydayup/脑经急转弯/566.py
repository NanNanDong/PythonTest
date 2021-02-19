# 重塑矩阵

from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        oldW = len(nums[0])
        oldH = len(nums)
        # print(oldW, oldH)
        if oldW * oldH != r * c: return nums
        res = []
        tmp = []
        for ns in nums:
            for n in ns:
                tmp.append(n)
                # print('--> ', n, c, len(tmp))
                if len(tmp) == c: 
                    res.append(tmp)
                    # print(tmp)
                    tmp = []
        return res

x = Solution()
print(x.matrixReshape([[1, 2], [3, 4]], 1, 4))