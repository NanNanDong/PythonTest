# 684. 冗余连接
# 破除环，形成树 --> 又是并查集

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodesCount = len(edges)
        parent = list(range(nodesCount + 1))

        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        
        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)
        
        for node1, node2 in edges:
            # 如果两个顶点属于不同的连通分量，则说明在遍历到当前的边之前，这两个顶点之间不连通，因此当前的边不会导致环出现，合并这两个顶点的连通分量。
            if find(node1) != find(node2):
                union(node1, node2)
            # 如果两个顶点属于相同的连通分量，则说明在遍历到当前的边之前，这两个顶点之间已经连通，因此当前的边导致环出现，为附加的边，将当前的边作为答案返回
            else:
                return [node1, node2]
        
        return []