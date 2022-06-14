# 1143. 最长公共子序列

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2) # m为横，n为纵

        res = 0

        # 0 是假设 空字符串 与任何字符串的最长公共子序列为0，所以下面遍历从 1 开始
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]: # 容易迷糊的点：dp的大小是大一圈的，首圈全是0
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return res

