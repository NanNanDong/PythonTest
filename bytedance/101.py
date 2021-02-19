# 101. 对称二叉树


from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def isMirror(p: TreeNode, q: TreeNode):
            if p == None and q == None: return True 
            if p == None or q == None: return False
            #  思考清楚后很容易
            return p.val == q.val and isMirror(p.left, q.right) and isMirror(p.right, q.left)

        return isMirror(root, root)

    # 这个好懂很多
    def isSymmetric1(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if not root:
			return True
		def dfs(left,right):
			# 递归的终止条件是两个节点都为空
			# 或者两个节点中有一个为空
			# 或者两个节点的值不相等
			if not (left or right):
				return True
			if not (left and right):
				return False
			if left.val!=right.val:
				return False
			return dfs(left.left,right.right) and dfs(left.right,right.left)
		# 用递归函数，比较左节点，右节点
		return dfs(root.left,root.right)


    # BFS
    def isSymmetric2(self, root: TreeNode) -> bool:

		if not root or not (root.left or root.right):
			return True
		# 用队列保存节点	
		queue = [root.left,root.right]
		while queue:
			# 从队列中取出两个节点，再比较这两个节点
			left = queue.pop(0)
			right = queue.pop(0)
			# 如果两个节点都为空就继续循环，两者有一个为空就返回false
			if not (left or right):
				continue
			if not (left and right):
				return False
			if left.val!=right.val:
				return False
			# 将左节点的左孩子， 右节点的右孩子放入队列
			queue.append(left.left)
			queue.append(right.right)
			# 将左节点的右孩子，右节点的左孩子放入队列
			queue.append(left.right)
			queue.append(right.left)
		return True


        



        