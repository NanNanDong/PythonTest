import java.util.ArrayList;
import java.util.List;

class Solution {

    // 按层遍历
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> order = new ArrayList<>();
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return order; 

        int rows = matrix.length, cols = matrix[0].length;
        // 层的边界值
        int left = 0, right = cols - 1, top = 0, bottom = rows - 1;

        while (left <= right && top <= bottom) {
            // 向右
            for (int column = left; column <= right; column++) {
                order.add(matrix[top][column]);
            }
            // 向下，初始化行为 top+1
            for (int row = top + 1; row <= bottom; row++) {
                order.add(matrix[row][right]);
            }
            // 向左和向上，先判断下
            if (left < right && top < bottom) {
                // right被用了，所以初始化right-1 
                for (int column = right - 1; column > left; column--) {
                    order.add(matrix[bottom][column]);
                }
                for (int row = bottom; row > top; row--) {
                    order.add(matrix[row][left]);
                }
            }
            
            left += 1;
            right -= 1;
            top +=1;
            bottom -=1;
        }

        return order;

    }
}