// 190. 颠倒二进制位

public class Solution {
    // 从低到高，按位颠倒
    public int reverseBits(int n) {
        int ans = 0;
        for (int i = 0; i < 32; i++) {
            int res = (n >> i) & 1; // 同0异1，适用于颠倒
            if (res == 1) {
                ans |= (1 << (31 - i)); // 加到结果上
            } 
        }
    }
}