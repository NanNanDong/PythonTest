# 701. 二叉搜索树中的插入操作

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # 画图模拟插入理解
    # 如果为空，直接返回新增节点；
    # 如果新增节点小于当前节点，左节点存在，迭代左节点；
    # 如果新增节点小于当前节点，左节点不存在，新增左节点，返回根节点；
    # 如果新增节点大于当前节点，右节点存在，迭代右节点；
    # 如果新增节点大于当前节点，右节点不存在，新增右节点，返回根节点；
    # https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/solution/python3-die-dai-bian-li-701-by-lionking8-pk3c/
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = TreeNode(val)
        if not root: return node

        dummyRoot = root

        while root:
            if val < root.val and root.left: # 左边不为空，往下迭代
                root = root.left
            elif val < root.val and not root.left: # 左边为空，见缝插针，返回头节点
                root.left = node
                return dummyRoot
            elif val > root.val and root.right:
                root = root.right
            elif val > root.val and not root.right:
                root.right = node
                return dummyRoot

