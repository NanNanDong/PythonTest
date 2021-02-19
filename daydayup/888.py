# 888. 公平的糖果棒交换
# 哈希表(两数之和变种)、双指针

from typing import List
class Solution:
    # def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
    #     sumA, sumB = sum(A), sum(B)
    #     delta = (sumA - sumB) // 2
    #     rec = set(A) # 如此简单的初始化
    #     ans = None

    #     for y in B:
    #         x = y + delta
    #         if x in rec:
    #             ans = [x, y]
    #             break
        
    #     return ans

    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sumA, sumB = sum(A), sum(B)
        delta = (sumA - sumB) // 2 # 注意这个差值取值，负数也OK
        i, j = 0, 0
        sortedA = sorted(A)
        sortedB = sorted(B)
        lenA = len(A)
        lenB = len(B)

        while i < lenA and j < lenB:
            cur = sortedA[i] - sortedB[j]
            if cur == delta: return [sortedA[i], sortedB[j]]
            elif cur > delta: j += 1
            else: i += 1

        return None



x = Solution()
print(x.fairCandySwap([1, 1], [2, 2]))

print(x.fairCandySwap([1, 2], [2, 3]))

print(x.fairCandySwap([2], [1, 3]))

print(x.fairCandySwap([2], [5, 3, 2]))



