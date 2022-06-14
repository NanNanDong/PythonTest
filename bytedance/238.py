# 238. 除自身以外数组的乘积

# 一定要看题意，就是求前/后缀积
# https://leetcode-cn.com/problems/product-of-array-except-self/solution/chu-zi-shen-yi-wai-shu-zu-de-cheng-ji-by-leetcode-/


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # L R 分别代表前缀积和后缀积
        L, R, res = [0] * n, [0] * n, [0] * n

        L[0] = 1
        for i in range(1, n):
            L[i] = nums[i - 1] * L[i - 1]
        
        R[n - 1] = 1
        for i in reversed(range(n - 1)): # 倒着遍历
            R[i] = nums[i + 1] * R[i + 1]

        # 对于索引 i，返回结果就是其前缀和后缀的积
        for i in range(n):
            res[i] = L[i] * R[i]

        return res


# 进阶到 O(1):
# 1.直接用前缀积填入到res中
# 2.遍历后缀的时候，一边遍历一边乘(计算后缀积)

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        # 合并前缀积到res作为初始化
        res[0] = 1
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        # 边遍历，边计算后缀积，得出结果
        R = 1
        for i in reversed(range(n)):
            res[i] = res[i] * R
            R *= nums[i]
        
        return res



    



x = Solution()
# print(x.productExceptSelf([1,2,3,4]))
print(x.productExceptSelf([-1,1,0,-3,3]))