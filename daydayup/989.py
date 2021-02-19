# 989. 数组形式的整数加法
# 不管两个数是列表形式，还是数组形式
# 公式： 当前位 = (A 的当前位 + B 的当前位 + 进位carry) % 10

from typing import List
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        carry = 0
        i = len(A) - 1
        res = []
        sum = 0

        while K or carry or i >= 0:
            if i >= 0: x = A[i] 
            else: x = 0
            if K != 0 : y = K % 10
            else: y = 0

            sum = int(x + y + carry)
            carry = int(sum / 10)

            K = int(K / 10)
            i -= 1
            res.insert(0, int(sum % 10)) # 直接添加到最前面

        if carry != 0: res.insert(0, carry)
        return res



x = Solution()
res = x.addToArrayForm([1,2,0,0], 34)
print(res)
