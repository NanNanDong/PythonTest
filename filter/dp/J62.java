package filter.dp;

// 每一个路径由其上一格和左一格决定

public class J62 {

    public static void main(String[] args) {
        Solution s = new Solution();
        s.uniquePaths(3, 7);
    }

    static class Solution {
        public int uniquePaths(int m, int n) {
            int[][] dp = new int[m][n];
            // 要初始化
            for (int i = 0; i < m; i++){
                dp[i][0] = 1;
            }

            for (int j = 0; j < n; j++){
                dp[0][j] = 1;
            }
            

            for (int i = 1; i < m; i++) {
                for (int j = 1; j < n; j++) {
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
                }
            }

            return dp[m - 1][n - 1];
        }
    }
    
}
