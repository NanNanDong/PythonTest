import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;

// Z字打印

class Solution {

    private TreeNode ans;

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
       dfs(root, p, q);
       return ans;
    }

    // 定义子问题：判断左右子树是否包含p、q，
    // 所以，这个递归有返回值
    private boolean dfs(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) return false;

        boolean lson = dfs(root.left, p, q);
        boolean rson = dfs(root.right, p, q);

        // 分别在 左子树 右子树
        // p或q就为root，则有一个在即可
        if ((lson && rson) || 
        ((root.val == p.val || root.val == q.val) && (lson || rson))) {
            ans = root;
        }

        // 恰好相等的情况也是表示存在的，不要遗漏！！！！！！！
        return lson || rson || (root.val == p.val || root.val == q.val);
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
