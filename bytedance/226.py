# 226. 翻转二叉树
# 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        # # 自顶向下
        # if not root: return
        # # 交换左右子树
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

        # 自底向上 --> 递归进去下面的先换
        if not root: return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
            
