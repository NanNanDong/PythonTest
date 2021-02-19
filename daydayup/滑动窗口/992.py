# 992. K 个不同整数的子数组
# 好子数组：连续、包含K个
# 思路点：
# 1.固定左边后，右指针一直移到不符合为主，right-start+1 就是最多包含k个的子数组数量
# 2.求恰好为k，则是用最多包含k个的子数组数量 - 最多包含k-1个子数组数量

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        n = len(A)
        num1, num2 = collections.Counter(), collections.Counter() # 我的话，哈希表了
        tot1 = tot2 = 0
        left1 = left2 = right = 0
        ret = 0

        for right, num in enumerate(A):
            if num1[num] == 0:
                tot1 += 1
            num1[num] += 1
            if num2[num] == 0:
                tot2 += 1
            num2[num] += 1
            
            while tot1 > K:
                num1[A[left1]] -= 1
                if num1[A[left1]] == 0:
                    tot1 -= 1
                left1 += 1
            while tot2 > K - 1:
                num2[A[left2]] -= 1
                if num2[A[left2]] == 0:
                    tot2 -= 1
                left2 += 1
            
            ret += left2 - left1
        
        return ret

