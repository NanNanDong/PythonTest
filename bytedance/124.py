# 124. 二叉树中的最大路径和

# 真的一点思路都没，虽然树肯定想到递归
# 想办法来个三选二

# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/er-cha-shu-zhong-de-zui-da-lu-jing-he-by-ikaruga/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self) -> None:
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        
        def maxGain(node: TreeNode) -> int:
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 计算左边分支最大值，左边分支如果为负数还不如不选择
            leftMax = max(maxGain(node.left), 0)
            # 计算右边分支最大值，右边分支如果为负数还不如不选择
            rightMax = max(maxGain(node.right), 0)

            # left->root->right 作为路径与已经计算过历史最大值做比较
            priceNewPath = node.val + leftMax + rightMax # --> 该节点的最大路径和

            self.maxSum = max(self.maxSum, priceNewPath)

            # 返回经过root的单边最大分支给当前root的父节点计算使用 --> 难点
            return node.val + max(leftMax, rightMax)

        maxGain(root)

        return self.maxSum


