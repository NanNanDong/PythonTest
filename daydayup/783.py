# 783. 二叉搜索树节点最小距离

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.res = float("inf")
        self.prev_val = -1

        def dfs(rt: TreeNode):
            if not rt: return
            dfs(rt.left)
            if self.prev_val != -1:
                self.res = min(self.res, (rt.val - self.prev_val))
            prev = rt.val
            dfs(rt.right)

        dfs(root)

        return self.res
