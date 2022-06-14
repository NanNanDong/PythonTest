/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
// 平衡二叉树：精髓在剪枝
class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) return true;
        boolean flag = Math.abs(height(root.left) - height(root.right)) <= 1; // 判断
        return flag && isBalanced(root.left) && isBalanced(root.right); // 这里会有很多重复计算       

    }

    // 辅助函数
    private int height(TreeNode root) {
        if (root == null) return 0;
        return Math.max((height(root.left)), height(root.right)) + 1;
    }




    public boolean isBalanced(TreeNode root) {
        return dfs(root) != -1;
    }

    // 辅助函数
    private int dfs(TreeNode root) {
        if (root == null) return 0;

        // 剪枝
        if (root == null) return 0;
        int left = dfs(root.left);
        if(left == -1) return -1;
        int right = dfs(root.right);
        if(right == -1) return -1;

        // 不符合提前特判返回
        return Math.abs(left - right) < 2 ? Math.max(left, right) + 1 : -1;
    }
}