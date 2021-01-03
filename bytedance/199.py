# 199. 二叉树的右视图
# 1. BFS：每层遍历的最右边的存入
# 2. DFS：根-右-左，可保证每层第一次访问的是右边的

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(root, depth):
            if not root:
                return
            if len(res) <= depth:
                res.append(0)
            res[depth] = root.val # 利用深度判断第一次进来的肯定是右边的
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)

        dfs(root, 0)
        
        return res

    def ightSideView2(self, root: TreeNode) -> List[int]:
        if not root : return []
        res = []

        def bfs(root):
            queue = [root]
            while queue:
                nxt = []
                res.append(queue[-1].val)
                for node in queue:
                    if node.left:
                        nxt.append(node.left)
                    if node.right:
                        nxt.append(node.right)
                queue = nxt
        
        bfs(root)
        return res