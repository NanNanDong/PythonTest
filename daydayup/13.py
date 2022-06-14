# 13. 罗马数字转整数

# 若一个数字右侧的数字比它大，则将该数字的符号取反

class Solution:
    def romanToInt(self, s: str) -> int:
        # map映射，注意和12题list的区别
        symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        }

        res = 0
        n = len(s)

        for i, ch in enumerate(s):
            value = symbols[ch]
            if i < n - 1 and value < symbols[s[i+1]]: # 本题核心就是找规律取反
                res -= value
            else:
                res += value
            
        return res

x = Solution()
print(x.romanToInt("III"))        








