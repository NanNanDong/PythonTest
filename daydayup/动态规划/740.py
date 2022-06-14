# 740. 删除并获得点数

# 小偷问题的变形
# 题目意思，明显dp，分选和不选

from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnts = [0] * 10009

        m = 0

        # 更新频率 + 计数
        for x in nums:
            cnts[x] += 1
            m = max(m, x)

        # f[i][0] 代表「不选」数值 i；f[i][1] 代表「选择」数值 i
        f = [[0] * 2 for _ in range(m + 1)] # 这个初始化

        for i in range(1, m + 1):
            f[i][1] = f[i - 1][0] + i * cnts[i] # 选择i
            f[i][0] = max(f[i - 1][1], f[i-1][0]) # 不选i，比较大小

        return max(f[m][0], f[m][1]) #最大这个数选不选，决定最大值
            

