import java.util.LinkedList;
import java.util.Queue;

// 958. 二叉树的完全性检验

class Solution958 {
    // 完全性校验，层序遍历，每层满的
    // public boolean isCompleteTree(TreeNode root) {
    // Queue<TreeNode> queue = new LinkedList<>();
    // queue.offer(root);

    // boolean reachEnd = false;

    // while (!queue.isEmpty()) {
    // TreeNode cur = queue.poll();

    // if (reachEnd && cur != null) return false;

    // if (cur == null) {
    // reachEnd = true;
    // continue;
    // }
    // queue.offer(cur.left);
    // queue.offer(cur.right);
    // }

    // return true;
    // }

    public static void main(String[] args) {
        Solution s = new Solution();
    }

    static class Solution {
        public boolean isCompleteTree(TreeNode root) {
            Queue<TreeNode> queue = new LinkedList<>();
            queue.offer(root);

            boolean reachEnd = false;

            while (!queue.isEmpty()) {
                TreeNode cur = queue.poll();

                if (cur == null) {
                    reachEnd = true;
                } else {
                    if (reachEnd) return false;
                    queue.offer(cur.left);
                    queue.offer(cur.right);
                }
            }

            return true;
        }

        public class TreeNode {
            int val;
            TreeNode left;
            TreeNode right;

            TreeNode() {
            }

            TreeNode(int val) {
                this.val = val;
            }

            TreeNode(int val, TreeNode left, TreeNode right) {
                this.val = val;
                this.left = left;
                this.right = right;
            }
        }

    }
}