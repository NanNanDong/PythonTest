# 54. 螺旋矩阵

from typing import List


class Solution:
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     # 边界极值
    #     left, top, right, bottom = 0, 0, (len(matrix) - 1), (len(matrix[0]) - 1 if matrix else 0)
    #     # 四个方向
    #     L, U, R, D = 1, 2, 3, 4
    #     direct = R

    #     i, j = 0, 0
    #     res = list()
    #     res.append(matrix[i][j])

    #     while left <= right and top <= bottom:
    #         if direct == R: # 向右
    #             if right >= j:
    #                 j += 1
    #                 res.append(matrix[i][j])
    #             if right == j:
    #                 top += 1 # 上面一行遍历完了
    #                 direct = D # 向下
    #         elif direct == D:
    #             if bottom >= i:
    #                 i += 1
    #                 res.append(matrix[i][j])
    #             if bottom == i:
    #                 right -= 1
    #                 direct = L
    #         elif direct == L:
    #             if left <= j:
    #                 j -= 1
    #                 res.append(matrix[i][j])
    #             if left == j:
    #                 bottom -= 1
    #                 direct = U
    #         elif direct == U:
    #             if top <= i:
    #                 i -= 1
    #                 res.append(matrix[i][j])
    #             if top == i:
    #                 left += 1
    #                 direct = R

    #     return res

    # 按层模拟
    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        
        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1): # 从左往右
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1): # 从上到下
                order.append(matrix[row][right])
            if left < right and top < bottom: # 符合往下遍历的条件
                for column in range(right - 1, left, -1): 
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1 # 往内缩一层
        return order

    # 直接模拟 + visited ,技巧性更多
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        
        rows, cols = len(matrix), len(matrix[0])
        visited = [[False] * cols for _ in range(rows)]
        total = rows * cols
        res = [0] * total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 四个方向
        row, col = 0, 0
        directionIndex = 0
        for i in range(total):
            res[i] = matrix[row][col]
            visited[row][col] = True

            nextRow, nextCol = row + directions[directionIndex][0], col + directions[directionIndex][1]
            if not (0 <= nextRow < rows and 0 <= nextCol < cols and not visited[nextRow][nextCol]):
                directionIndex = (directionIndex + 1) % 4 # 周而复始
            
            # 往下遍历
            row += directions[directionIndex][0]
            col += directions[directionIndex][1]
            
        return res





x = Solution()
print(x.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
                
                    
                
            



