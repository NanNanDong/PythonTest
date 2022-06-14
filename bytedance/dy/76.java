import java.security.KeyStore.Entry;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

// 最小覆盖子串 
// 滑动窗口

// 1.暴力：遍历大于t长度的，频数大于t的
// 2.滑动窗口：当前已经满足（更大的不会符合），则移动左边界
// 辅助函数：两个map，右边map的频数满足，移动的时候改变用O(1)记录
// 滑动窗口的字符频数map，t的字符频数map
class Solution {
    public String minWindow(String s, String t) {
        HashMap<Character, Integer> tFreq = new HashMap<>();
        char[] tArray = t.toCharArray();
        int tLen = tArray.length;
        for (int i = 0; i < tLen; i++) {
            tFreq.put(tArray[i], tFreq.getOrDefault(tArray[i], 0) + 1);
        }
        HashMap<Character, Integer> winFreq = new HashMap<>();

        int len = Integer.MAX_VALUE;
        int ansL = -1, ansR = -1; // 答案
        int sLen = s.length();
        int l = 0, r = 0; // 窗口

        char[] sArray = s.toCharArray();
        while (r < sLen) {
            if (check(winFreq, tFreq)) {
                l++;
                ansL++;
                winFreq.put(sArray[l], winFreq.getOrDefault(sArray[l], 0)-1);
            }
            r++;
            winFreq.put(sArray[r], winFreq.getOrDefault(sArray[r], 0)+1);
            if (check(winFreq, tFreq)) {
                ansR++;
                
            }
        }
    }

    // 用distance维护，可以改成O(1)
    public boolean check(HashMap<Character, Integer> winFreq, HashMap<Character, Integer> tFreq) {
        for (Map.Entry<Character, Integer> entry: tFreq.entrySet()) {
            if (winFreq.get(entry.getKey()) < entry.getValue()) {
                return false;
            }
        }
        return true;
    }


}