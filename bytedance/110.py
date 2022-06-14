# 110. 平衡二叉树
# 左树和右树的高度差为1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 自顶向下，暴力
    def isBalanced(self, root: TreeNode) -> bool:

        # 高度辅助函数
        def depth(root) -> int:
            if not root: return 0
            return max(depth(root.left), depth(root.right)) + 1

        if not root: return True
        rootRes = (abs(depth(root.left) - depth(root.right)) <= 1)
        return rootRes and self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced(self, root: TreeNode) -> bool:
        





