# 48. 旋转图像
# https://leetcode-cn.com/problems/rotate-image/solution/xuan-zhuan-tu-xiang-by-leetcode-solution-vu3m/
# 1.辅助数组，matrix[i][j] = matrix_new[j][n-i-1] --> 优化，如何避免覆盖原值(每次交换轮回，涉及4个数字)
# 2.水平翻转后，主对角线翻转
from typing import List


class Solution:
    # def rotate1(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     n = len(matrix)

    #     res = [[0] * n for _ in range(n)]

    #     for i in range(n):
    #         for j in range(n):
    #             res[j][n-i-1] = matrix[i][j]
        
    #     matrix[:] = res # 数组赋值

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2): # 一半就行，不然不是转回去了
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        
        # 主对角线翻转
        for i in range(n):
            for j in range(i): # 坑点
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        

    

    