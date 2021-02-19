# 1203. 项目管理
# 两层拓扑排序(组/项目): 从入度为0度开始，然后更新其相邻的入度(拓扑排序的结果不唯一)
# ---> 题：207/210

import collections
from typing import List

class Solution:
    def tp_sort(self, items, indegree, neighbors):
        q = collections.deque([])
        ans = []
        for item in items:
            if not indegree[item]:
                q.append(item)
        while q:
            cur = q.popleft()
            ans.append(cur)

            for neighbor in neighbors[cur]:
                indegree[neighbor] -= 1
                if not indegree[neighbor]:
                    q.append(neighbor)

        return ans

    def sortItems(self, n: int, m: int, group: List[int], pres: List[List[int]]) -> List[int]:
        max_group_id = m
        for project in range(n):
            if group[project] == -1:
                group[project] = max_group_id
                max_group_id += 1

        project_indegree = collections.defaultdict(int)
        group_indegree = collections.defaultdict(int)
        project_neighbors = collections.defaultdict(list)
        group_neighbors = collections.defaultdict(list)
        group_projects = collections.defaultdict(list)

        for project in range(n):
            group_projects[group[project]].append(project)

            for pre in pres[project]:
                if group[pre] != group[project]:
                    # 小组关系图
                    group_indegree[group[project]] += 1
                    group_neighbors[group[pre]].append(group[project])
                else:
                    # 项目关系图
                    project_indegree[project] += 1
                    project_neighbors[pre].append(project)

        ans = []

        group_queue = self.tp_sort([i for i in range(max_group_id)], group_indegree, group_neighbors)

        if len(group_queue) != max_group_id:
            return []

        for group_id in group_queue:

            project_queue = self.tp_sort(group_projects[group_id], project_indegree, project_neighbors)

            if len(project_queue) != len(group_projects[group_id]):
                return []
            ans += project_queue

        return ans


# 链接：https://leetcode-cn.com/problems/sort-items-by-groups-respecting-dependencies/solution/tu-jie-tuo-bu-pai-xu-1203-xiang-mu-guan-4xrll/
