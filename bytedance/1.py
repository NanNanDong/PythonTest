# 两数之和，只对应一个答案
class Solution(object):
    def twoSum(self, nums, target):
        nMap = dict()
        for index, num in enumerate(nums): # 记住这种遍历写法
            nMap[num] = index
        for i, num in enumerate(nums):
            j = nMap[target - num]
            if j is not None and i != j:
                return[i, j]

    def twoSum1(self, nums, target):
        nMap = dict()
        for i, num in enumerate(nums):
            if target - num in nMap:
                return [nMap[target-num], i]
            nMap[nums[i]] = i
        return []
