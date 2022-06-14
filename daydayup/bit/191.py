# 191. 位1的个数

# 算术右移 >> ：舍弃最低位，高位用符号位填补；
# 逻辑右移 >>> ：舍弃最低位，高位用 0 填补。

class Solution:
    # 右移 32 次
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1 # 二进制末尾是否是1 --> & 000001
            n >> 1
        return res

    # 库函数
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

    # n & (n - 1) 可以把n的二进制中 最后一个出现的 1 改写成 0
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n & n -1
        return res
    
    

    

