# 232. 用栈实现队列

class MyQueue:
    def __init__(self):
        self.stack1 = [] # 主栈
        self.stack2 = [] # 辅助栈


    def push(self, x: int) -> None:
        self.stack1.append(x)


    def pop(self) -> int:
        _s1 = self.stack1
        _s2 = self.stack2
        if not _s2: # 辅助栈不为空
            while _s1:
                _s2.append(_s1.pop())
        return _s2.pop()



    def peek(self) -> int:
        _s1 = self.stack1
        _s2 = self.stack2
        if not _s2: 
            while _s1:
                _s2.append(_s1.pop())
        return _s2[-1]



    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

