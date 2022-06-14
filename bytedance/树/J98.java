import java.util.ArrayList;
import java.util.List;

class Solution {
    // public boolean isValidBST(TreeNode root) {
    //     return dfs(root, Long.MIN_VALUE, Long.MAX_VALUE);
    // }

    // private boolean dfs(TreeNode root, long lower, long upper) {
    //     if (root == null) return true;

    //     // 不在范围内是错的
    //     if (node.val <= lower || node.val >= upper){
    //         return false;
    //     }

    //     return dfs(root.left, lower, node.val) && dfs(root.right, node.val, upper);
    // }



    public boolean isValidBST(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        dfs(root, res);

        if (res.size() <= 1) return true;
        for (int i = 1; i < res.size(); i++) {
            if (res.get(i) <= res.get(i - 1)) {
                return false;
            }
        }
        return true;
    }


    private void dfs(TreeNode root, List<Integer> res) {
        if (root == null) return;

        dfs(root.left, res);
        res.add(root.val);
        dfs(root.right, res);
    }

}