# 207. 课程表
# 广度优先：操作入度
# 深度优先：判断是否有环
# 通过课程前置条件列表 prerequisites 可以得到课程安排图的 邻接表 adjacency，以降低算法时间复杂度
from collections import deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        # Get the indegree and adjacency of every course.
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # Get all the courses with the indegree of 0.
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)
        # BFS TopSort.
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1 # 是真正从邻接表中删除此节点 pre，而是将此节点对应所有邻接节点 cur 的入度 -1−1
                if not indegrees[cur]: queue.append(cur)
        return not numCourses



    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): return False
        return True

x = Solution()
x.canFinish(2, [[1,0],[0,1]])
x.canFinish(2, [[1,0]])