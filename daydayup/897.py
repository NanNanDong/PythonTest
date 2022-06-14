# 897. 递增顺序搜索树

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.res = []

        def dfs(root: TreeNode):
            if not root: return
            dfs(root.left)
            self.res.append(root)
            dfs(root.right)

        dfs(root)

        if not self.res: return

        dummyHead = TreeNode(-1)
        cur = dummyHead
        for n in self.res:
            n.left = n.right = None # 不要左右子树
            cur.right = n
            cur = cur.right
            
        return dummyHead.right

            



       
