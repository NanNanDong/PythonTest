# 395. 至少有 K 个重复字符的最长子串

# for循环遍历一次是26个字符，循环里面对 ss 分割时间复杂度是O(N)O(N)
# 这是道递归，不能用滑动窗口

# 重点：
# 如果一个字符 c 在 s 中出现的次数少于 k 次，
# 那么 s 中所有的包含 c 的子字符串都不能满足题意。
# 所以，应该在 s 的所有不包含 c 的子字符串中继续寻找结果

# 不要用脑子去想递归

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        for c in set(s): # s 直接转成set
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c)) # 在 s 的所有不包含 c 的子字符串中继续寻找结果
        
        return len(s)

s = "cs2zscvs"
print(s.count("c"))
print(s.count("s"))
print(s.count("2"))
print(s.count("1"))

    