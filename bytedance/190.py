# 190. 颠倒二进制位
# 位运算的基本问题

# 取出 n 的最低位，加入结果 res 中。然后 n 右移，res 左移。循环此过程
class Solution:
    def reverseBits(self, n: int) -> int:
        res, count = 0, 32
        while count:
            res <<= 1
            # 取出 n 的最低位数加到 res 中
            res += n&1
            n >> 1
            count -= 1

        # return int(bin(res), 2)
        return res

x = Solution()
print(x.reverseBits(43261596))