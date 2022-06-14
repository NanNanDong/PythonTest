package bytedance.字符串;

import java.util.HashMap;
import java.util.HashSet;


class Solution {

    // 暴力解法
    // 1.逐个生成子字符串
    // 2.看它是否包含重复字符串
    public int lengthOfLongestSubstring(String s) {
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
                String sub = s.substring(i, j);
                HashSet set = new HashSet<>();
                for (int k = 0; k < sub.length(); k++) {
                    if (set.contains(sub.charAt(k))) {
                        break;
                    } {
                        set.add(sub.charAt(k));
                    }
                }
                res = Math.max(res, sub.length());   
            }
        }
        return res;
    }

    // 模式识别，关键字：
    // 重复字符 --> 散列表
    // 子串 --> 滑动窗口
    public int lengthOfLongestSubstring1(String s) {
        int len = s.length();
        if (len == 0)
            return 0;

        HashMap<Character, Integer> map = new HashMap<Character, Integer>(len);

        int left = 0, right = 0; // 左指针
        int max = 0; // 返回值

        while (right < len) {
            Character c = s.charAt(right);

            if (map.containsKey(c)) {
                // ！！！！ 思路点 ！！！！
                // 举例：有记录的后一个与当前窗口起始位置比较(因为当前有记录的可能已经不再窗口内了)
                // 不能直接赋值，因为要维持这个left的含义
                // 1.若直接赋值为 right + 1，right - left + 1 得到的值就小了，
                // 因为他前面的可能是可以计入长度的
                // 2.若直接赋值为 map.get(c) + 1，可能会回跳到前面，导致上一个判重失效
                left = Math.max(left, map.get(c) + 1);
            }

            // 扩展窗口
            map.put(c, right);
            max = Math.max(max, right - left + 1);

            right++;
        }

        return max;
    }
}