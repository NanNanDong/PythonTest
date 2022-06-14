# 224. 基本计算器

# 只有乘除和括号
# 这题最大思维点，就是理解计算机处理为什么是 num1 num2 + 这样的比较快

# https://leetcode-cn.com/problems/basic-calculator/solution/ji-ben-ji-suan-qi-by-leetcode-solution-jvir/
# ops的取值确实得推论
# 如果当前位置处于一系列括号之内，则也与这些括号前面的运算符有关：每当遇到一个以 - 号开头的括号，则意味着此后的符号都要被「翻转」
# ---> ops首尾存正负号，后面放括号
# 这个思路其实不太舒服

# https://leetcode-cn.com/problems/basic-calculator/solution/ru-he-xiang-dao-yong-zhan-si-lu-lai-zi-y-gpca/
# 遇到左括号的时候要存一存，遇到右括号要处理

from os import stat


class Solution:
    def calculate1(self, s: str) -> int:
        ops = [1]
        sign = 1

        res = 0

        n = len(s)
        i = 0

        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                res += num * sign
        
        return res

    def calculate(self, s: str) -> int:
        res, num, sign = 0, 0, 1 # num作为计算过程数
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == '+' or c == '-':
                res += sign * num
                num = 0
                sign = 1 if c == "+" else -1 # sign后面更新
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        
        res += sign * num
        return res





