# 155. 最小栈

import math

class MinStack:
    
    def __init__(self):
        self.stk = []
        self.min_stk = [math.inf]


    def push(self, x: int) -> None:
        self.stk.append(x)
        # 辅助栈存储较小的即可，pop的时候也能直接pop
        # 逻辑顺畅些，在pop的时候判断下是否为相同
        self.min_stk.append(min(x, self.min_stk[-1])) 

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()


    def top(self) -> int:
        return self.stk[-1]


    def getMin(self) -> int:
        return self.min_stk[-1]


