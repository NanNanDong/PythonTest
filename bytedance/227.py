# 227. 基本计算器 II

# 先乘除后加减，栈存储

# 加号：将数字压入栈；
# 减号：将数字的相反数压入栈；
# 乘除号：计算数字与栈顶元素，并将栈顶元素替换为计算结果

class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stk = []
        preSign = '+'
        num = 0

        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if i == n - 1 or s[i] in '+-*/':
                if preSign == '+':
                    stk.append(num)
                elif preSign == '-':
                    stk.append(-num)
                elif preSign == '*':
                    stk.append(stk.pop() * num)
                else:
                    stk.append(int(stk.pop() / num))
                
                preSign = s[i]
                num = 0
        
        return sum(stk)