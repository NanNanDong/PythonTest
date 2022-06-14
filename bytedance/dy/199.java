import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

// 右侧
// BFS：每一层的最后一个节点
// DFS：加入辅助depth，首次size==depth时add，右视图先右再左
class Solution {

    // BFS
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null) return ans;

        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            // 加入一层
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);

                if (i == size - 1) ans.add(node.val);
            }
        }

        return ans;
    }


    // DFS
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        dfs(root, 0, ans);
        return ans;
    }

    private void dfs(TreeNode root, int depth, List<Integer> ans) {
        if (root == null) return;

        // 相等的时候add
        if (ans.size() == depth) {
            ans.add(root.val);
        }

        depth++;
        dfs(root.left, depth, ans);
        dfs(root.right, depth, ans);
    }



    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
  }
}