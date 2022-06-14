import org.graalvm.compiler.lir.LIRInstruction.Temp;

// 114. 二叉树展开为链表

// 展开为前序遍历
 
class Solution {

    // https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/114-er-cha-shu-zhan-kai-wei-lian-biao-by-ming-zhi-/    
    public void flatten(TreeNode root) {
        while (root != null) {
            if (root.left == null) {
                root = root.right;
            } else {
                // 找左子树最右边的节点
                TreeNode pre = root.left;
                while (pre.right != null) pre = pre.right;

                // 将原来的右子树接到左子树的最右边
                pre.right = root.right;
                // 将左子树插入到右子树的地方
                root.right = root.left;
                root.left = null;
                // 考虑下一个节点
                root = root.right;
            }
        }
    }

    public void flatten(TreeNode root) {
        if (root == null) return;

        flatten(root.left);
        flatten(root.right);

        // 左边拖到右边
        TreeNode tmp = root.right;
        root.right = root.left;
        // 左边置空
        root.left = null;

        // 找到当前最右边的，把右边设置过去
        while (root.right != null) root = root.right;
        root.right = tmp;
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