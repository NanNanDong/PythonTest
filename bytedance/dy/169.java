import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

// 169. 多数元素

class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> freqMap = new HashMap<Integer, Integer>();
        int size = nums.length;
        for (int i = 0; i < nums.length; i++) {
            int freq = freqMap.getOrDefault(nums[i], 0) + 1;
            if (freq > size / 2) return nums[i];
            freqMap.put(nums[i], freq);
        }
        return -1;
    }

    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }

    

}