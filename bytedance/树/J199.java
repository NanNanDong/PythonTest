import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {

    List<Integer> res = new ArrayList<>();

    // 1.DFS 根-右-左 第一次遍历到的depth
    public List<Integer> rightSideView(TreeNode root) {
        dfs(root, 0);
        return res;
    }

    private void dfs(TreeNode root, int depth) {
        if (root == null) return;
        if (depth == res.size()) res.add(root.val);
        dfs(root.right, depth+1);
        dfs(root.left, depth+1);
    }

    // BFS 
    public List<Integer> rightSideView1(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while(!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (node.left != null) 
                    queue.add(node.left);
                if (node.right != null) 
                    queue.add(node.right);
                // size-1为一层里的第一个
                if (i == size-1) 
                    res.add(node.val);
            }
        }
        return res;
    }

    

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }
}