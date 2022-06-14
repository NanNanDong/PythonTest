class Solution {
    // 贪心，取每个上升
    public int maxProfit(int[] prices) {
        int res = 0;
        for (int i = 1; i < prices.length; i++) {
            res += Math.max(0, prices[i] - prices[i-1]);
        }

        return res;
    }

    public int maxProfit(int[] prices) {
        int len = prices.length;
        int[][] dp = new int[len][2];

        // dp[i][0] 第i天，卖出后手上持有的钱
        dp[0][0] = 0; // 卖出股票
        dp[0][1] = -prices[0]; // 买入股票

        for (int i = 1; i < len; i++) {
            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]); // 前：前一天没有股票，后：持有才能卖
            dp[i][1] = Math.max(dp[i-1][1], dp[i-1][0] - prices[i]); // 前：前一天有股票，后：前面没有才能买
        }

        return dp[len-1][0];
    }
}