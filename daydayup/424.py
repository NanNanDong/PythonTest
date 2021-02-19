# 424. 替换后的最长重复字符
# 1.移动到k用完，替换非最多的

# https://leetcode-cn.com/problems/longest-repeating-character-replacement/solution/ti-huan-hou-de-zui-chang-zhong-fu-zi-fu-eaacp/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        num = [0] * 26
        n = len(s)
        maxCount = left = right = 0

        while right < n:
            num[ord(s[right]) - ord("A")] += 1
            maxCount = max(maxCount, num[ord(s[right]) - ord("A")]) # ord是python返回ascii码的函数
            if right - left + 1  > maxCount + k:
                num[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1

        return right - left

x = Solution()
print(x.characterReplacement("ABAB", 2))




