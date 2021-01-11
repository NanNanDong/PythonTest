# 236. 二叉树的最近公共祖先:节点唯一
# 很简单的一道递归题：
# 终止条件：1. 越过叶子节点，直接返回null 2. root等于p或q，则直接返回
# 递归：1. 递归左子节点，返回left 2. 递归右子节点，返回right
# 返回：1. l、r同时为空，root的左右子树都不包含p，q，返回null；
#      2. l、r同时不为空，则p，q分列在root的两侧
#      3. l为空，r不为空，则返回r，反之亦然

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q : return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root

    # 好理解些
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return root
        if root.val == p.val or root.val == q.val: return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root
        if l: return l
        if r: return r