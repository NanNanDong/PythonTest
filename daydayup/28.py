# 28. 实现 strStr()
# KMP

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        
        if n > m: return -1
        for i in range(m - n + 1):
            if haystack[i: i + n] == needle:
                return i
        return -1

    



x = Solution()
# print(x.strStr("a", "a"))
# print(x.strStr("a", ""))
# print(x.strStr("hello", "ll"))
# print(x.strStr("aaaaa", "bba"))
print(x.strStr("mississippi", "issip"))
