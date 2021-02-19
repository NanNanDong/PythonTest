# 344. 反转字符串

from typing import List
import math
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lenz = len(s)
        size = math.floor(lenz / 2)
        # size = int(5 / 2)
        # size = math.ceil(5 / 2)

        for i in range(size):
            print(i)
            s[i], s[lenz - i - 1] = s[lenz - i - 1], s[i]

        print(s)


        
x = Solution()
x.reverseString(x.reverseString(["h","e","l","l","o"]))