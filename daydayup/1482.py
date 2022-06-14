# 1482. 制作 m 束花所需的最少天数

from typing import List

import heapq

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m > len(bloomDay) / k:
            return -1
        
        # 辅助函数，不同天的开花结果，连续k朵，能做m束花
        def canMake(days: int) -> bool:
            bouquets = flowers = 0
            for i, bloom in enumerate(bloomDay):
                if bloomDay[i] <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        if bouquets == m:
                            break
                        flowers = 0
                else:
                    flowers = 0
            return bouquets == m
        
        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            days = (low + high) // 2
            if canMake(days):
                high = days
            else:
                low = days + 1
        return low




    # def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
    #     n = len(bloomDay)

    #     num = m * k

    #     if (num > len(bloomDay)): return -1

    #     heap = []

    #     for i in bloomDay:
    #         heapq.heappush(heap, i)
    #         print(heap)
    #         if len(heap) >= num:
    #             heapq.heappop(heap)

    #     return heapq.heappop(heap)


x = Solution()
print(x.minDays([1,10,3,10,2], 3, 1))

