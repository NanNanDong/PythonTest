# 338. 比特位计数
# 虽然看题意明显知道应该是DP，但数1都还不会

# https://leetcode-cn.com/problems/counting-bits/solution/pythondong-tai-gui-hua-yi-ci-bian-li-qin-52gq/

from typing import List


class Solution:
    def countBits1(self, num: int) -> List[int]:
        def countOnes(x: int) -> int:
            ones = 0
            while x > 0:
                x &= (x - 1)
                ones += 1
            return ones
        res = [countOnes(i) for i in range(num + 1)]
        return res

# print(2 ** 4) # ** 是阶乘

    def countBits(self, num: int) -> List[int]:
        dp = [0, 1]
