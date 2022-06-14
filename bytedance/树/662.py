# 662. 二叉树最大宽度
# 每个节点都有一个position的值,若一个结点是x,那该节点的左子节点是2x,右子节点是2x+1,始终保持这样的关系

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        left = {}

        def dfs(node: TreeNode, depth: int, pos: int):
            if node:
                # 对于每一个深度，第一个到达的位置会被记录在 left[depth] 中
                left.setdefault(depth, pos)
                # print(pos)
                # 对于每一个节点，它对应这一层的可能宽度是 pos - left[depth] + 1
                res = max(res, pos - left[depth] + 1)
                dfs(node.left, depth + 1, pos * 2)
                dfs(node.right, depth + 1, pos * 2 + 1)
        
        dfs(root,0, 0)

        return res
