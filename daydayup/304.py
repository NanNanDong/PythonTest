# 304. 二维区域和检索 - 矩阵不可变

# 会多次调用region就提示了，可以运用线段相减
# 前缀和

from typing import List


class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix) # 列数量
        n = len(matrix[0]) if matrix else 0
        self.sums = [[0] * (n + 1) for _ in range(m + 1)] # 先都初始化为0

        _sums = self.sums
        # print(_sums)

        # 难点在这个前缀的构建 -> 其实也不难，有点dp的味道，两块相加减去重复加的，加上当前坐标
        for i in range(m):
            for j in range(n):
                _sums[i + 1][j + 1] = _sums[i][j + 1] +  _sums[i + 1][j] - _sums[i][j] + matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sum = self.sums
        # 随便画个图就知道，是大块减去左边和上边两个小块，加上对角多减的一小块
        return _sum[row2 + 1][col2 + 1] - _sum[row1][col2 + 1] - _sum[row2 + 1][col1] + _sum[row1][col1]



x = NumMatrix([
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
])
