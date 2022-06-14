
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        sgn = 1 if x > 0 else -1
        Max = 2**31 - 1 if sgn == 1 else 2**31
        
        x, res = abs(x), 0
        
        while x:
            digit = x % 10 # digit为取得末尾数字
            x = x // 10
            # 需要 res*10+digit<=Max 如果超界 中途返回
            # 超界条件 res*10+digit>Max 等价于 digit/10>(Max/10-res)
            # 需要保证反转后的数字在范围内，但假定计算机存储不了
            if digit / 10 > (Max / 10 - res): return 0
            res = res * 10 + digit
        
        return res * sgn

x = Solution()
print(x.reverse(123))


