// 415. 字符串相加

// 长度判断
class Solution {
    public String addStrings(String num1, String num2) {
        int acc = 0;
        int i = num1.length();
        int j = num2.length();

        StringBuilder ans = new StringBuilder();
        while (i >= 0 || j >= 0 || acc > 0) {
            int x = i >= 0 ? num1.charAt(i) - '0' : 0;
            int y = j >= 0 ? num2.charAt(j) - '0' : 0;
            int res = x + y + acc;
            ans.append(res % 10);
            acc = res / 10;
            i--;
            j--;
        }
        ans.reverse();
        return ans.toString();
    }
}