# 554. 砖墙

# https://leetcode-cn.com/problems/brick-wall/solution/chi-xiao-dou-xun-lian-jie-ti-si-lu-rang-wbgfx/

from typing import List
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        mp = defaultdict(int)
        m = len(wall)

        tmp = 0
        for i in range(m):
            for j in range(len(wall[i]) - 1):
                tmp += wall[i][j]
                mp[tmp] += 1

        return m - max(mp.values(), default=0)
        # res = m
        # for i, c in mp:
        #     res = min(res, res - c)
        
        # return res


        prefixSum = defaultdict(int)

        n = len(wall)
        for i in range(0, n):

            currSum = 0
            # 每一行砖的最后一列不要计算进来, 否则会把最右侧的垂直线考虑进去
            for j in range(0, len(wall[i]) - 1):
                # 计算每一行的砖的宽度和
                currSum += wall[i][j]
                # 如果有相同的前缀和, 这里会+1
                prefixSum[currSum] += 1
        # 总高度 减去 前缀和数量最多的
        return n - max(prefixSum.values(), default=0)


