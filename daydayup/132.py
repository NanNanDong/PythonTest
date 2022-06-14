# 132. 分割回文串 II

# 难就难在这里必须dp了
# https://leetcode-cn.com/problems/palindrome-partitioning-ii/solution/xiang-tong-de-si-lu-cong-zui-chang-di-ze-9kfm/

# 巧妙的思路：就是求最长递增子序列，只是把判断条件改成是否回文了

class Solution:
    def minCut(self, s):
        def isPalindrome(substring: str) -> bool:
            return substring == substring[::-1]

        n = len(s)
        dp = [n] * n

        for i in range(n):
            if isPalindrome(s[0:i+1]):
                dp[i] = 0
                continue
            for j in range(i):
                if isPalindrome(s[j+1:i+1]):
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n - 1]



    # def minCut(self, s: str) -> int:

    #     def isPalindrome(substring: str) -> bool:
    #         if substring == substring[::-1]: return True
    #         else: return False
        
    #     res = []

    #     if not s : return res

    #     def dfs(remain, tmp):
    #         if len(remain) == 0:
    #             res.append(tmp)
            
    #         for i in range(len(remain)):
    #             left = remain[:i+1]
    #             right = remain[i+1:]
    #             if isPalindrome(left):
    #                 dfs(right, tmp+1)
    #             else:
    #                 continue
        
    #     dfs(s, 0)
    #     return min(res) - 1

x = Solution()
print(x.minCut("aab"))
print(x.minCut("a"))
print(x.minCut("ab"))
