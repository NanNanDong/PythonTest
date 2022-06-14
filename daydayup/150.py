# 150. 逆波兰表达式求值

# 逆序数，常用技巧：归并排序
# 或者高级数据结构：离散化树状数组

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # 难点是这个lambda的定义

        op_to_binary_fn = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": lambda x, y: int(x / y),   # 需要注意 python 中负数除法的表现与题目不一致
        }

        stack = list()
        for token in tokens:
            # 巧妙的利用try..except
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_to_binary_fn[token](num1, num2)
            finally:
                stack.append(num)
            
        return stack[0]







