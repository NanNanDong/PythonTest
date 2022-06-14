# 59. 螺旋矩阵 II

# 就模拟，左下右上顺序，设置边界，到了以后，边界更新
# 难点在于写出来
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, t, r, b = 0 , 0, n - 1, n - 1
        res = [[0 for _ in range(n)] for _ in range(n)] # 初始化的骚操作牢记

        num, max = 1, n * n

        while num <= max:
            # left -> right
            for i in range(l, r + 1):
                res[t][i] = num # 思维卡壳点，横坐标是t
                num += 1
            t += 1 # 要更新遍历过的上边界

            for i in range(t, b + 1):
                res[i][r] = num
                num += 1
            r -= 1

            for i in range(r, l - 1, -1): # l-1的位置不会被更新到
                res[b][i] = num
                num += 1
            b -= 1

            for i in range(b, t - 1, -1):
                res[i][l] = num
                num += 1
            l += 1

        return res






