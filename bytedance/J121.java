package bytedance;

// 题目具有特殊性，min是必须要选的，所以更新min后，一直和min取差就好了
class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        int min = prices[0];

        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < min) {
                min = prices[i];
            } else {
                res = Math.max(res, prices[i] - min);
            }
        }
        return res;
    }

    // // DP
    // public int maxProfit(int[] prices) {
    //     int len = prices.length;
        
    //     int[][] dp = new int[len][2];

    //     // dp[i][0] 表示这天不买
    //     // dp[i][1] 表示这天买

    //     dp[0][0] = 0;
    //     dp[0][1] = -prices[0];

    //     for (int i = 1; i < len; i++) {
    //         dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]);
    //         dp[i][1] = Math.max(dp[i-1][1], -prices[i]); 
    //     }
    //     return dp[len - 1][0];
    // }

}