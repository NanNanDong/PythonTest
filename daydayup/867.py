# 867. 转置矩阵

# 转置矩阵就是把M行N列的矩阵，转成N行M列的矩阵，
# 原来矩阵中 matrix[i][j]matrix[i][j] 的位置，
# 会交换到新矩阵的 res[j][i]res[j][i] 位置


from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        transposed = [[0] * m for _ in range(n)] 
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        return transposed


x = Solution()
print(x.transpose([[1,2,3],[4,5,6],[7,8,9]]))


