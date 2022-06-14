# 213. 打家劫舍 II

# dp
# f[i][0] 代表考虑前 i 个房间，并且「不选」第 i 个房间的最大价值。
# 由于已经明确了第 i 个房间不选，因此 f[i][0] 可以直接由 max(f[i−1][0],f[i−1][1]) 转移而来。

# f[i][1] 代表考虑前 i 个房间，并且「选」第 ii 个房间的最大价值。
# 由于已经明确了第 i 个房间被选，因此 f[i][1] 直接由 f[i - 1][0] + nums[i]f[i−1][0]+nums[i] 转移过来。

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1: return nums[0]

        # 肯定不选第一间
        f = [[0] * 2 for _ in range(n)]
        for i in range(1, n - 1):
            f[i][0] = max(f[i - 1][0], f[i - 1][1]) # i间不选
            f[i][1] = f[i - 1][0] + nums[i] # 选i间
        a = max(f[n - 2][1], f[n - 2][0] + nums[n - 1])

        # 允许选第一间
        f[0][0], f[0][1] = 0, nums[0]
        for i in range(1, n - 1):
            f[i][0] = max(f[i - 1][0], f[i - 1][1])
            f[i][1] = f[i - 1][0] + nums[i]
        b = max(f[n - 2][0], f[n - 2][1])

        return max(a, b)

        