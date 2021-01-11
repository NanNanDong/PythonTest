# 228. 汇总区间

from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0: return []
        res = []
        preNum = nums[0]
        lastNum = nums[0]
        for i in range(1, n):
            if nums[i] - lastNum > 1:
                if preNum == lastNum:
                    res.append(str(lastNum))
                else:
                    res.append(str(preNum) + "->" + str(lastNum))
                preNum = nums[i]

            lastNum = nums[i]

        # 最后手动加了次判断感觉有点蠢
        if preNum == lastNum:
            res.append(str(lastNum))
        else:
            res.append(str(preNum) + "->" + str(lastNum))
        return res

    def summaryRanges1(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        i = 0
        while i < n:
            low = i
            i += 1
            while i < n and nums[i] == nums[i -1] + 1: # 巧妙的i<n将结尾合进去了
                i += 1
            high = i - 1
            tmp = str(nums[low])
            if low < high:
                tmp = tmp+"->"+str(nums[high])
            res.append(tmp)
        return res



x = Solution()
l = x.summaryRanges1([0,1,2,4,5,7])
print(l)
                


