# 766. 托普利茨矩阵
# 这种简单，横纵坐标都有规律的

from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        w = len(matrix[0])
        h = len(matrix)
        # print(w, h)

        for i in range(1, h):
            for j in range(1, w):
                # print(matrix[i][j], i, j)
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        
        return True

x = Solution()
print(x.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))

