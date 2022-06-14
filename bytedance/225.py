# 队列实现栈

import collections

from collections import deque
class MyStack:
    def __init__(self):
        self.data = deque()
        self.help = deque()

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        while len(self.data) > 1:
            self.help.append(self.data.popleft())
        tmp = self.data.popleft()        
        self.help,self.data = self.data,self.help
        return tmp

    def top(self) -> int:
        while len(self.data) != 1:
            self.help.append(self.data.popleft())
        tmp = self.data.popleft()
        self.help.append(tmp)
        self.help,self.data = self.data,self.help
        return tmp

    def empty(self) -> bool:
        return not bool(self.data)


class MyStack:
    
    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()


    def push(self, x: int) -> None:
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1


    def pop(self) -> int:
        return self.queue1.popleft()


    def top(self) -> int:
        return self.queue1[0]


    def empty(self) -> bool:
        return not self.queue1



# 单队列，拿头放到尾巴
# n = len(self.queue)
# self.queue.append(x)
# for _ in range(n):
#     self.queue.append(self.queue.popleft())


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()