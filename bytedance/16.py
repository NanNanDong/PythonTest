# 最接近的三数之和

# https://leetcode-cn.com/problems/3sum-closest/solution/zui-jie-jin-de-san-shu-zhi-he-gao-xiao-j-ag9d/

# 排序+双指针
# 排序后，选取第一个为i，l 为 i+1，r 为 length-1


from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')

        n = len(nums)

        for i in range(n - 2):
            # 特殊用例，如[0,0,0], range(1, n-1)不过
            if i >= 1 and nums[i] == nums[i - 1]: # 跳过重复元素
                continue

            left = i + 1 # 左指针
            right = n - 1 # 右指针

            while left < right:
                # 当前和与 target 的差值
                cur_diff = nums[i] + nums[left] + nums[right] - target
                if cur_diff == 0:
                    return target
                if cur_diff > 0: # 大于target，左移右指针
                    right -= 1
                else:
                    left += 1
                
                # 更新最小值(有符号的)
                min_diff = cur_diff if abs(cur_diff) < abs(min_diff) else min_diff

        return target + min_diff


x = Solution()
# print(x.threeSumClosest([0,0,0],1))
print(x.threeSumClosest([-1,2,1,-4],1))