# 173. 二叉搜索树迭代器

# 1.保存中序遍历的结果 --> 没利用到搜索树
# 2.双色遍历法，第一次入栈为白色，第二次为灰色，第二次出栈(和节点上画3个点异曲同工)
# https://leetcode-cn.com/problems/binary-search-tree-iterator/solution/li-kou-jia-jia-jian-dan-yi-dong-de-san-s-kryk/

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class BSTIterator:

#     def __init__(self, root: TreeNode):
#         self.queue = collections.deque()
#         self.inOrder(root)

#     def inOrder(self, root: TreeNode):
#         if not root: return
#         self.inOrder(root.left)
#         self.queue.append(root.val)
#         self.inOrder(root.right)


#     def next(self) -> int:
#         return self.queue.popleft()


#     def hasNext(self) -> bool:
#         return len(self.queue) > 0


class BSTIterator:
    
    def __init__(self, root: TreeNode):
        self.stack = [(root, 0)]       


    def next(self) -> int:
        while True:
            node, color = self.stack.pop()
            if color == 1: return node.val
            if node.right: self.stack.append((node.right, 0))
            self.stack.append((node, 1))
            if node.left: self.stack.append((node.left, 0))

    def hasNext(self) -> bool:
        return len(self.stack) > 0