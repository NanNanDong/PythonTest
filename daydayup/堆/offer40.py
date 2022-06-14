# 剑指 Offer 40. 最小的k个数

# 最小的K个，用大顶堆
# Python中的堆为小根堆，因此我们要对数组中所有的数取其相反数，才能使用小根堆维护前k小值。

from typing import List
import heapq

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0: return list()

        heap = [-x for x in arr[:k]]

        heapq.heapify(heap)

        for i in range(k, len(arr)):
            if -heap[0] > arr[i]: # 负数比较大，则原来的正数值比较小 --> 保持堆的大小为k
                heapq.heappop(heap) # 弹出第一个
                heapq.heappush(heap, -arr[i])
        
        res = [-x for x in heap] # 转回正数
        return res

