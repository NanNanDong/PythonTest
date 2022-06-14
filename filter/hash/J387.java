package filter.hash;

import java.security.KeyStore.Entry;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

public class J387 {
    

    static class Solution {
        public int firstUniqChar(String s) {

            HashMap<Character, Integer> charMap = new HashMap<>();
            HashMap<Character, Integer> charIdx = new HashMap<>();

            
            for (int i = 0; i < s.length(); i++) {
                Character c = s.charAt(i);
                charMap.put(c, charMap.getOrDefault(c, 0) + 1);
                if (!charIdx.containsKey(c)) {
                    charIdx.put(c, i);
                }
            }

            int minIdx = s.length() + 1;
            for (Map.Entry<Character, Integer> e: charMap.entrySet()) {
                if (e.getValue() == 1) {
                    minIdx = Math.min(minIdx, charIdx.get(e.getKey()));
                }
            }

            if (minIdx == s.length() + 1) return -1; else return minIdx;
        }
    }

}
