# 1232. 缀点成线
# 按照坐标算斜率就好了，唯一注意的是不能除以0，所以换乘法就好了
# dy2/dx2 = dy1/dx1 ---> dx1*dy2 = dx2*dy2


from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0] # 第一个的坐标
        x1, y1 = coordinates[1]
        dx1, dy1 = x1 - x0, y1 - y0
        for i in range(2, len(coordinates)):
            dx2, dy2 = coordinates[i][0] - x0, coordinates[i][1] - y0
            if dx1 * dy2 != dy1 * dx2:
                return False
        return True

x = Solution()
print(x.checkStraightLine([[0,0],[0,1],[0,-1]]))