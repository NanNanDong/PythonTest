# 12. 整数转罗马数字

class Solution:

    def intToRoman(self, num: int) -> str:
        symbols = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"), ]
        
        roman = list()

        # 这样写比较安全
        for value, symbol in symbols:
            while num >= value:
                num -= value
                roman.append(symbol)
            if num == 0:
                break
        
        return "".join(roman)
