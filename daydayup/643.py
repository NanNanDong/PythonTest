# 643. 子数组最大平均数 I
# 双指针(滑动窗口)、dp

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxTotal = total = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            total = total - nums[i - k] + nums[i]
            maxTotal = max(maxTotal, total)
        
        return maxTotal / k


