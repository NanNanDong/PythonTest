# 331. 验证二叉树的前序序列化

# https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/solution/pai-an-jiao-jue-de-liang-chong-jie-fa-zh-66nt/

# 1.栈，遇到数字，消掉两个，append回去一个(且栈顶第三个不为#)
# 2.由上面，可以推断，出入度和为0

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')

        v = 1 # 因为根节点，初始化入度为1

        for n in nodes:
            v -= 1
            if v < 0:
                return False
            if n != '#':
                v += 2
        
        return v == 0

    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')

        stk = []

        for node in nodes:
            stk.append(node)

            while len(stk) >= 3 and stk[-1] ==  stk[-2] == '#' and stk[-3] != '#':
                stk.pop(), stk.pop(), stk.pop()
                stk.append('#')
            
        return len(stk) == 1 and stk[-1] == '#'
    


