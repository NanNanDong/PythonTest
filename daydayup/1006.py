# 1006. 笨阶乘

# https://leetcode-cn.com/problems/clumsy-factorial/solution/ben-jie-cheng-by-leetcode-solution-deh2/
# 求解经验，表达式一般可以借助栈
# 遇到乘除立即算，遇到加减先入栈

import operator

class Solution:
    def clumsy(self, N: int) -> int:
        op = 0
        stack = [N]

        for i in range(N - 1, 0, -1):
            if op == 0:
                stack.append(stack.pop() * i)
            elif op == 1:
                # python的除法有坑，或者 int(num1 / float(num2)) ,先用浮点数除法，然后取整
                stack.append(int(operator.truediv(stack.pop(), i)))
            elif op == 2:
                stack.append(i)
            elif op == 3:
                stack.append(-i)
            
            op = (op + 1) % 4 # 巧妙的规划 加减乘除

        return sum(stack)



