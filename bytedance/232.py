# 232. 用栈实现队列
# pop时，先把stack1中的元素移向stack2，stack1为1时，仅剩1个时，为需要返回的元素

class MyQueue:
    def __init__(self):
        self.stack1 = [] # 主栈
        self.stack2 = [] # 辅助栈

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        res = self.stack1.pop()
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return res
        
    def peek(self) -> int:
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        res = self.stack1.pop()
        self.stack2.append(res)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return res
    
    def empty(self) -> bool:
        return len(self.stack1) == 0
            