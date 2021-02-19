# 1018. 可被 5 整除的二进制前缀
from typing import List
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        tmp = 0
        res = []
        for num in A:
            tmp = tmp * 2 + num
            res.append(tmp % 5 == 0)
        
        return res

    def prefixesDivBy5_1(self, A: List[int]) -> List[bool]:
        res = []
        prefix = 0
        for num in A:
            prefix = ((prefix<<1) + num) % 5 # 解决溢出
            res.append(prefix == 0)
        return res

x = Solution()
print(x.prefixesDivBy5([0,1,1]))
print(x.prefixesDivBy5([1,1,1]))
print(x.prefixesDivBy5([0,1,1,1,1,1]))
print(x.prefixesDivBy5([1,1,1,0,1]))

