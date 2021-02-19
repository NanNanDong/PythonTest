# 105. 从前序与中序遍历序列构造二叉树
# 为啥节点数值唯一？ 可以保证下标和数值唯一对应
# 

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 只要我们在中序遍历中定位到根节点，那么我们就可以分别知道左子树和右子树中的节点数目。由于同一颗子树的前序遍历和中序遍历的长度显然是相同的，因此我们就可以对应到前序遍历的结果中
        def myBuildTree(preLeft: int, preRight: int, inLeft: int, inRight: int):
            if preLeft > preRight: return None

            # 前序遍历第一个节点就是根节点
            preRoot = preLeft
            # 在中序遍历中定位根节点
            inRoot = index[preorder[preRoot]]

            # 先把根节点建立出来
            root = TreeNode(preorder[preRoot])
            # 得到左子树的节点数目
            leftTreeSize = inRoot - inLeft
            # 递归的构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preLeft + 1, preLeft + leftTreeSize, inLeft, inRoot - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preLeft + leftTreeSize + 1, preRight, inRoot + 1, inRight)
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0 , n - 1)
