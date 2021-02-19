# 448. 找到所有数组中消失的数字
# 1.排序 --> 一样，除非原地排序
# 2.哈希
# 3.原地修改数组：遍历到nums[i]把第nums[i]−1位置的元素 乘以-1
# ---> 属于奇淫巧技
# 扩展：若是 每个数字都出现了2次，只有一个数字出现了1次 --> 异或
from typing import List

class Solution:
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        counter = set(nums) # 真香！

        res = []
        n = len(nums)

        # print(nums)

        for i in range(1, n + 1):
            # print(i)
            if i not in counter:
                # print(i)
                res.append(i)
        
        return res

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            newIndex = abs(nums[i]) - 1
            if nums[newIndex] > 0:
                nums[newIndex] *= -1
        for j in range(len(nums)):
            if nums[j] > 0:
                res.append(j + 1)
        return res


x = Solution()
print(x.findDisappearedNumbers([4, 3, 2, 7, 8, 3, 1]))
