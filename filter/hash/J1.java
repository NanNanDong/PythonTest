package filter.hash;

import java.util.HashMap;

// 可以边put边判断

public class J1 {

    public static void main(String[] args) {
        Solution s = new Solution();
        s.twoSum(new int[]{3, 2, 4}, 6);
    }

    static class Solution {

        public int[] twoSum(int[] nums, int target) {
            HashMap<Integer, Integer> map = new HashMap<>();

            // HashSet存储元素
            for (int i = 0; i < nums.length; i++) {
                map.put(nums[i], i);
            }

            // 遍历查找
            for (int j = 0; j < nums.length; j++) {
                if (map.containsKey(target - nums[j])) { // 找到对应的
                    int targetIdx = map.get(target-nums[j]);
                    if (targetIdx != j)
                        return new int[] {j, targetIdx};
                }
            }

            return new int[] {0, 0};
        }

    }
    
}
