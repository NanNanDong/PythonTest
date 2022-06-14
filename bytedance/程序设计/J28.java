public class J28 {

    class Solution {
        public int strStr(String haystack, String needle) {
            int n = haystack.length(), m = needle.length();

            for (int i = 0; i + m <= n; i++) { // 避免循环溢出
                boolean flag = true; // 前置设置找到了
                for (int j = 0; j < m; j ++) {
                    if (haystack.charAt(i + j) != needle.charAt(j)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    return i;
                }
            }

            return -1;
        }
    }

}
