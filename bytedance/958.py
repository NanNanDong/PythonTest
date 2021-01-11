# 958. 二叉树的完全性检验
# 1. 树的size 是否 等于 最后一个节点的indexCode
# 推导过程：如果不为空，则利用完全二叉树性质
# 2. 前一个为null，后一个不为null时，才不是不是完全二叉树

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        nodes = [(root,1)] 
        i = 0
        while i < len(nodes):
            node, v = nodes[i] # 将序号赋值给v
            i += 1
            if node:
                nodes.append((node.left, 2 * v))
                nodes.append((node.right, 2 * v + 1))
        return nodes[-1][1] == len(nodes)

x = Solution()
l = TreeNode(1, None, None)
x.isCompleteTree(l)