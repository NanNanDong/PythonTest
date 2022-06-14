# 938. 二叉搜索树的范围和

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.res = 0

        def dfs(r: TreeNode, low: int, high: int):
            if not r :return

            dfs(r.left, low, high)
            
            if root.val > high: return # 剪枝
            if low <= r.val <= high:
                self.res += r.val

            dfs(r.right, low, high)

        dfs(root, low, high)

        return self.res

class Solution(object):
    def rangeSumBST(self, root, low, high):
        res = 0
        if not root:
            return res
        if root.val > low:
            res += self.rangeSumBST(root.left, low, high)
        if low <= root.val <= high:
            res += root.val
        if root.val < high:
            res += self.rangeSumBST(root.right, low, high)
        return res

