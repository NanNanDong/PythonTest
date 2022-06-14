import java.util.LinkedList;
import java.util.Queue;

// https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree/solution/ceng-xu-bian-li-by-dian-dao-de-hu-die-681d/

class Solution {

    // 层序遍历，只应该遇到一次空节点，且为结束节点
    public boolean isCompleteTree(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root); // offer添加到队列

        boolean reachEnd = false;

        while (!queue.isEmpty()) {
            TreeNode cur = queue.poll();
            
            // 只应该结尾的时候为null
            if (reachEnd && cur != null) {
                return false;
            } 

            // 避免结束进来的空
            if (cur == null) {
                reachEnd = true;
                continue;
            }

            queue.offer(cur.left);
            queue.offer(cur.right);
        }
        
        return true;
    }

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
   }
}
