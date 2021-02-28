# 896. 单调数列

# 既遇到了递增有遇到递减就退出

from typing import List


class Solution:
    # def isMonotonic(self, A: List[int]) -> bool:
    #     n = len(A)
    #     if n <= 1: return True
    #     diff = A[n - 1] - A[0]

    #     if diff > 0 :
    #         for i in range(1, n):
    #             if A[i] < A[i - 1]: return False
    #     else:
    #         for i in range(1, n):
    #             if A[i] > A[i - 1]: return False
        
    #     return True

     def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if n <= 1: return True

        upFlag = False
        downFlag = False
        for i in range(1, n):
            if A[i] > A[i - 1]:
                upFlag = True
                if downFlag: return False
            elif A[i] < A[i - 1]:
                downFlag = True
                if upFlag: return False
        
        return True

x = Solution()
print(x.isMonotonic([1, 2, 2, 3]))
print(x.isMonotonic([6, 5, 5, 4]))
print(x.isMonotonic([1, 3, 2]))
print(x.isMonotonic([1, 2, 4, 5]))
print(x.isMonotonic([1, 1, 1]))