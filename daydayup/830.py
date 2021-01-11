# 830. 较大分组的位置
# 使用num记录重复字符的个数
from typing import List
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        # res = list() # 记住python就是这么方便
        res = []
        n, num = len(s), 1
        if(n < 3) : return res 
        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                if num >= 3:
                    res.append([i - num + 1, i])
                num = 1
            else:
                num += 1
        return res

x = Solution()
print(x.largeGroupPositions("abbxxxxzzy"))

# x = "abbxxxxzzy"
# print(x[2])
