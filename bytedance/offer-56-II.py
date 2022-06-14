# 剑指 Offer 56 - II. 数组中数字出现的次数 II

# 只有一个1次，其余3次

# https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/solution/mian-shi-ti-56-ii-shu-zu-zhong-shu-zi-chu-xian-d-4/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            else:
                d[num] += 1

        for key,value in d.items:
            if value == 1:
                return key

    # 有限状态机
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        # 这个得对位运算极其熟练
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        
        return ones
    

x = Solution()
print(x.singleNumber([3,4,3,3]))

