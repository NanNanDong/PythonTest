# 145. 二叉树的后序遍历

# 迭代实现后序遍历

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     res = list()

    #     def postOrder(root: TreeNode):
    #         if root == None: return None
    #         postOrder(root.left)
    #         postOrder(root.right)
    #         res.append(root.val)

    #     postOrder(root)

    #     return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return list()

        res = list()
        stack = list()
        prev = None
        # 必须有画图，不然很难理解
        while root or stack:
            while root:
                stack.append(root) 
                root = root.left # 把根、左节点加进来，到不能往左遍历为止
            root = stack.pop() # 弹出第一个(最左边的)开始操作
            if not root.right or root.right == prev: # 没有右节点，且标记了没遍历过的，进行输出操作
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root) # 往右边进行遍历
                root = root.right
        
        return res

    # 前序遍历好理解，反过来就是后序遍历了！
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                res.append(node.val) 
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        
        return res[::-1]





    
