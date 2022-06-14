# 264. 丑数 II
# 1. 每次取出堆顶元素x，则x是堆中最小堆丑数，由于2x、3x、5x也是丑数，因此也加入堆
#  --> 巧妙堆避免了2*2小于5的插队问题
# 2. 哈希去重
# 3. 第n次从最小堆中取元素则为第n个丑数
# python只支持最小堆 --> heapq

import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [2, 3, 5]
        seen = {1} # 去重哈希
        heap = [1] # 初始化堆

        for i in range(n - 1):
            curr = heapq.heappop(heap) # 弹出堆顶元素
            for n in nums:
                if (nxt := curr * n) not in seen: # pyhonic写法
                    seen.add(nxt)
                    heapq.heappush(heap, nxt) # 往堆里添加元素
                    # print(heap)
                
        return heapq.heappop(heap)


x = Solution()
print(x.nthUglyNumber(10))