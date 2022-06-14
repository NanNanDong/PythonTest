# 剑指 Offer 32 - III. 从上到下打印二叉树 III

# 之字形打印二叉树

import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 层序遍历 + 双端队列（奇偶层逻辑分离） / 层序遍历 + 偶数层倒序
    def levelOrder(self, root):
        if not root: return []

        res, deque = [], collections.deque([root])

        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2: tmp.appendleft(node.val) # 偶数层，添加到队列头部
                else: tmp.append(node.val) # 奇数层，添加到队列尾部

                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)

            res.append(list(tmp))

        return res





