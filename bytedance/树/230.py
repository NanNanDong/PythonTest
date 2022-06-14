# 二叉搜索树中第K小的元素

# 1.利用中序排序，其就是从小到大大排列

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        res = []

        def inorder(r: TreeNode):
            if not r: return

            inorder(r.left)
            res.append(r.val)
            inorder(r.right)

        inorder(root)

        return res[k - 1]

    # 借助栈迭代，可以加速，不必遍历整个树
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []

        while True:
            while root: # 左，体会下这里是用while一扎到底
                stack.append(root)
                root = root.left
            
            # 中，进行操作
            root = stack.pop()

            k -= 1
            if k == 0:
                return root.val
            
            # 右，加入右边
            root = root.right

