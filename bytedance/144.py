# 144. 二叉树的前序遍历

# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def preOrder(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            preOrder(root.left)
            preOrder(root.right)
        
        preOrder(root)
        return res

