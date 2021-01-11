# 189. 旋转数组
# 1. 使用额外的数组
# 2. 环状替换：gcd(最大公约数) --> 太数学化了(类似于利用数学关系，经过多少次交换，最后会交换完)
# 3. 数组翻转：这个就比较正常的解法了
#     1. 翻转所有元素
#     2. 翻转[0, k -1]区间 --> 因为k可能大于数组长度，所以是 k%n
#     3. 翻转[k, n-1]区间
# python数组翻转的三种实现：list(reversed(nums))、sorted(nums, reverse=True)、nums[::-1]
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # print(nums[::-1])
        # print(list(reversed(nums)))
        # print(sorted(nums, reverse=True))
        n = len(nums)
        k %= n
        # nums[::-1]
        # print(nums)
        nums[0:n] = reversed(nums[0:n]) # 可以用start : end 表示数组里的一个区间( i >= start and i < end) --> 故不用-1，和java前开后闭区相反
        # print(nums)
        nums[0:k] = reversed(nums[0:k])
        # print(nums)
        nums[k:n] = reversed(nums[k:n])
        # print(nums)


    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        newNums = [0]*n
        for i in range(n):
            newNums[(i+k)%n] = nums[i]
        
        for j in range(n): # 数组不能直接赋值
            nums[j] = newNums[j]


    

x = Solution()
x.rotate([1,2,3,4,5,6,7], 3)