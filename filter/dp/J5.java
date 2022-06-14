package filter.dp;

// 连续的 最大子序和

public class J5 {

    class Solution {
        public int maxSubArray(int[] nums) {
            int n = nums.length;
            int pre = 0;
            int max = nums[0];
            
            for (int i = 0; i < n; i++) {
                pre = Math.max(nums[i] + pre, nums[i]); // 之前的加上当前的数字 和 当前数字 取较大
                max = Math.max(pre, max);
            }

            return max;
        }
    }
    
}
