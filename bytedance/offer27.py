# 剑指 Offer 27. 二叉树的镜像

# 递归入门中的入门
# 不要用脑子想递归，
# 就是对右边的子树递归，赋值给左树
# 对左边的子树递归，赋值给右树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root == None: return None
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root

