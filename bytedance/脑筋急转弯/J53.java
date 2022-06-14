import java.util.Collections;

class Solution {
    // 动态规划
    public int maxSubArray(int[] nums) {
        // 前一个元素大于0，则加到当前元素上
        int n = nums.length;

        for (int i = 1; i < n; i++) {
            if (nums[i - 1] > 0) {
                nums[i] += nums[i - 1];
            }
        }
        
        int res = nums[0];
        for (int num : nums){
            if (num > res) res = num;
        }
        return res;
    }

    public int maxSubArray(int[] nums) {
        // 前一个元素大于0，则加到当前元素上
        int n = nums.length;
        int max = nums[0];
        int[] dp = new int[n];

        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(0, dp[i-1]+nums[i]);
            max = Math.max(dp[i], max);
        }
        return max;
    }

    // 贪心，如果sum<0，另起炉灶
    public int maxSubArray(int[] nums) {
       //特判
       if(nums == null || nums.length == 0) return 0;
       //初始化
       int curSum = 0;
       int maxSum = Integer.MIN_VALUE;
       //遍历
       int len = nums.length;
       for(int i = 0; i < len; i++){
           curSum += nums[i];      //计算curSum
           maxSum = Math.max(maxSum,curSum);   //更新maxSum
           if(curSum < 0){     //更新curSum
               curSum = 0;
           }        
       }
       return maxSum;
    }
}