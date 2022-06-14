# 179. 最大数

from typing import List

# 化繁为简，根据两个值比较，来判断排序
# 要点是写法了

import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = map(str, nums)

        def cmp(a: int, b: int):
            if a + b == b + a:
                return 0
            elif a + b > b + a: # 前面的大
                return 1
            else:
                return -1
        
        # print(nums)
        # print(strs)
        strs = sorted(strs, key=functools.cmp_to_key(cmp), reverse=True)
        # print(strs)
        
        res = "".join(strs)
        # 小细节，全是0，返回 0000
        if res[0] == '0':
            res = '0'
        return res

x = Solution()
print(x.largestNumber([3,30,34,5,9]))


    
