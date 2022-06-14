// 121. 买卖股票的最佳时机

class Solution {
    public int maxProfit(int[] prices) {
        int min = prices[0];
        int ans = 0;
        int n = prices.length;

        for (int i = 0; i < n; i++) {
            if (prices[i] < min) {
                min = prices[i];
            }
            ans = Math.max(prices[i] - min, ans);
        }

        return ans;
    }
}