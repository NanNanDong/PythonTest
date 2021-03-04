# 303. 区域和检索 - 数组不可变

# 前缀和优化！
# sumRange(i,j)=sums[j+1]−sums[i]

from typing import List


# class NumArray:
    
#     s_nums = List[int]

#     def __init__(self, nums: List[int]):
#         self.s_nums = nums

#     def sumRange(self, i: int, j: int) -> int:
#         if i < 0 or j > len(self.s_nums): return -1
#         res = 0
#         for x in range(i ,j + 1):
#             # print(self.s_nums[x])
#             res += self.s_nums[x]
#         return res

# class NumArray:
#     def __init__(self, nums: List[int]):
#         self.sums = [0]

#         for num in nums:
#             self.sums.append(self.sums[-1] + num)

#     def sumRange(self, i: int, j: int) -> int:
#         return self.sums[j + 1] - self.sums[i]

class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = [0]
        _sum = self.sums

        for num in nums:
            _sum.append(_sum[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        _sum = self.sums
        return _sum[j + 1] - _sum[i]


x = NumArray([-2, 0, 3, -5, 2, -1])
print(x.sumRange(0, 2))
print(x.sumRange(2, 5))
print(x.sumRange(0, 5))