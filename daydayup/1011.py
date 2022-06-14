# 1011. 在 D 天内送达包裹的能力

# 贪心 + 二分
# 1.封装一个方法，限制载重为x，顺序贪心添加，返回最少天数
# 2.二分查找目的载重

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r = max(weights), sum(weights) # 初始范围 载重量不能低于任何一个包裹的重量
        while l < r:
            mid = (l + r) // 2
            day = self.min_segments(weights, mid)

            if day <= D: # D天正好或有空余 一定注意 不是r=mid-1
                r = mid
            elif day > D: # D天不足 说明承载量太少需要增加
                l = mid + 1
        return l
            

    # 限制重量为 limit ，按顺序添加，返回天数
    def min_segments(self, weights: List[int], limit: int) -> int:
        n = len(weights)
        cum = 0
        num_D = 1 # 初始化为1
        i = 0
        for i in range(n):
            if cum + weights[i] <= limit:
                cum += weights[i] # 添加必须要放在判断后面 没有超过再加
            else: # 如果超重
                num_D += 1 # 运输+1天
                cum = weights[i] # 重置累计重量
            i += 1
        return num_D

        
