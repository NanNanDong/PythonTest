// 最长回文子串

// 子串 != 子序列
// DP

class Solution {
    // 暴力
    public String longestPalindrome(String s) {
        int len = s.length();
        if (len < 2) return s;

        // 通过maxLen减少回文判断
        // 通过begin剪枝
        int maxLen = 1;
        int begin = 0;
        char[] charArray = s.toCharArray(); // 转成array数组

        // 枚举所有长度大于1的子串
        for (int i = 0; i < len - 1; i++) { // 倒数第二个即可
            for (int j = i+1; j < len; j++) { // 从i+1位置开始
                // 通过长度剪枝
                int size = j - i + 1;
                if (j-i+1 > maxLen && validPalindromic(charArray, i, j)) {
                    maxLen = size;
                    begin = i; // 记录begin
                }
            }
        }
        return s.substring(begin, begin+maxLen);
    }

    public boolean validPalindromic(char[] charArray, int left, int right) {
        while (left < right) {
            if (charArray[left] != charArray[right]) return false;
            left++;
            right--;
        }
        return true;
    }

    // 中心扩散法 --> 也是暴力


    // 动态规划
    // 去掉头尾也是回文
    // 状态：dp[i][j] 表示子串s[i..j]是否是回文
    // 状态转移方程：dp[i][j] == (s[i]==s[j]) and dp[i+1][j-1]
    // 边界条件：j-1-(i+1)+1<2 即 j-i<3 （子串长度为2或3，不用检查）
    // 初始化：dp[i][i]=true
    public String longestPalindrome(String s) {
        int len = s.length();
        if (len < 2) return s;

        int maxLen = 0;
        int begin = 0;
        
        boolean[][] dp = new boolean[len][len];

        for (int i = 0; i < len; i++) {
            dp[i][i] = true; // 对角线置为0，长度为1的都是回文串
        }

        char[] charArray = s.toCharArray();

        // 递归
        // 枚举子串长度
        for (int width = 2; width <= len; width++) {
            for (int i = 0; i< len; i++) {
                // 🈶由宽和i，就可以得出右边界：j-i+1=width
                int j = width + i - 1;
                if (j >= len) break;

                if (charArray[i] != charArray[j]) {
                    dp[i][j] = false;
                } else {
                    if (j-i < 3) { // 长度限制，必回文，剪枝
                        dp[i][j] = true;
                    } else {
                        dp[i][j] = dp[i+1][j-1]; //减去头尾推导过来
                    }
                }

                // 最长长度的维护
                int size = j-i+1;
                if (dp[i][j] && size > maxLen) {
                    maxLen = size;
                    begin = i; 
                }
            }
        }

        return s.substring(begin, begin+maxLen);
    }


    // 比manacher算法

}