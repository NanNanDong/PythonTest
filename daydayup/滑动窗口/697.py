# 697. 数组的度
# 目的是找到能取到最大度的最小连续子数组
# 记录起始pos、最后pos、count
from typing import List
from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        countDict, firstDict,lastDict = defaultdict(int), defaultdict(int), defaultdict(int) # 需要统计的三个字典
        # print(countDict)

        for i, num in enumerate(nums):
            countDict[num] += 1
            if num not in firstDict:
                firstDict[num] = i # 第一次出现，只更新一次
            lastDict[num] = i # 最后一次出现，不断更新
        
        maxFeq = max(countDict.values()) # 不用滑窗
        res = len(nums) # 最大就是数组长度

        for num in nums:
            if countDict[num] == maxFeq:
                maxLen= lastDict[num] - firstDict[num] + 1
                res = min(res, maxLen)

        return res


x = Solution()
print(x.findShortestSubArray([1,2,2,3,1,4,2]))