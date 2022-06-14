# 7. 整数反转

# 关键点：
# 1.判断整数的正负
# 2.判断反转后的整数是否溢出
# 步骤：
# 1.整数转为字符串
# 2.分别处理正负情况
# 3.根据是否溢出，返回相应值

class Solution:

    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            x = int('-' + s[1:][::-1])
        else:
            x = int(s[::-1])
        
        return x if (-2 ** 31) < x < (2 ** 31 - 1) else 0

    # 算数
    def reverse(self, x: int) -> int:
        res = 0
        flag = 1
        if x < 0:
            x = -x
            flag = -flag

        while x != 0:
            cur = x % 10
            res = res * 10 + cur
            x //= 10

        res = flag * res

        return res if (-2 ** 31) < res < (2 ** 31 - 1) else 0

    

x = Solution()
print(x.reverse(123))
print(x.reverse(-123))
print(x.reverse(120))