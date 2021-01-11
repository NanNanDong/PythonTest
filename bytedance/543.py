# 543. 二叉树的直径
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1

        def depth(node: TreeNode):
            if not node: return 0
            l = depth(node.left)
            r = depth(node.right)
            self.ans = max(self.ans, l + r + 1) # 及时更新
            return max(l, r) + 1
        
        depth(root)
        return self.ans - 1

