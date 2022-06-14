# 73. 矩阵置零

# O(m∗n) 和 O(m+n)O 空间的解法都十分简单，无非是「同等大小的矩阵」或「与行列数量相等的标识」来记录置零信息
# 1.先遍历，将遇到0的行列置为0；然后将对应的数据置为0
# 2.拿第一行和列来存储，额外判断下第一行

from typing import List


class Solution:
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row, col = [False] * m, [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        r0_flag, c0_flag = False, False

        # 找第一行是否有0
        for j in range(n):
            if matrix[0][j] == 0:
                r0_flag = True
                break

        # 找第一列是否有0
        for i in range(m):
            if matrix[i][0] == 0:
                c0_flag = True
                break
        
        # 把第一行和列作为标志位 --> 首行，前面判断过了
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        #print(matrix)
        # 置0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 处理记录的首行数据
        if r0_flag:
            for j in range(n):
                matrix[0][j] = 0
        
        if c0_flag:
            for i in range(m):
                matrix[i][0] = 0

                
    

