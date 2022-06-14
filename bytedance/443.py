# 443. 压缩字符串

# 双指针，边读边扫描，读到末尾或者下一位不为c，则更新锚点
# 注意是原地排序，结果要看的
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        anchor = write = 0
        n = len(chars)
        for i, c in enumerate(chars):
            # print(i, c)
            if i + 1 == n or chars[i + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if i > anchor: # 说明不止1
                    for digit in str(i - anchor + 1): # python大法好，不用//10了
                        chars[write] = digit
                        write += 1
                anchor = i + 1 # 更新锚点

        return write



x = Solution()
# print(x.compress(["a","a","b","b","c","c","c"]))
print(x.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
