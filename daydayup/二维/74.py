# 74. 搜索二维矩阵

# https://leetcode-cn.com/problems/search-a-2d-matrix/solution/fu-xue-ming-zhu-liu-chong-fang-fa-bang-n-e20z/

# 利用矩阵性质：从左下角或者右上角开始查找

from typing import List

class Solution:
    # 首尾相连二分查找
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n -1

        while l <= r:
            mid = (l + r) >> 1
            x, y = mid // n, mid % n 
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False








