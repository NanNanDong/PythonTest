import java.util.HashMap;
import java.util.HashSet;

// 无重复字符的最长子串

// 无重复：散列表（index），子串：滑动窗口

// 1.暴力 O(N*N*N)，遍历所有子串，判重
// 2.滑动窗口 O(N)

// 思维要点：收缩时，当前字符可能已经不在窗口里

class Solution {

    public int lengthOfLongestSubstring(String s) {
        int ans = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        int left = 0;
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i); // 当前字符
            if (map.containsKey(c)) {
                // 当前左边界和map里的next比较
                left = Math.max(left, map.get(c)+1);
            }
            map.put(c, i); // 更新map的index
            ans = Math.max(ans, i-left+1); // 更新结果
        }
        return ans;  
    }
}