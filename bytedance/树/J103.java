import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;

// Z字打印

class Solution {

    // 层序遍历
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (root == null) return res;

        LinkedList<TreeNode> queue = new LinkedList<>();

        // 构造第一层
        queue.addLast(root);
        queue.addLast(null); // 添加分界符，表示该层结束！！！

        LinkedList<Integer> levelList = new LinkedList<>();
        boolean isReverse = false;

        while (queue.size() > 0) {
            // 弹出和压入
            TreeNode cur = queue.pollFirst();

            // 处理当前节点的值
            if (cur != null) {
                // 模板写法，思考一下，确实是，反正压在后面
                if (cur.left != null) {
                    queue.add(cur.left);
                }
                if(cur.right != null) {
                    queue.add(cur.right);
                }

                if (isReverse) {
                    levelList.addFirst(cur.val);
                } else {
                    levelList.addLast(cur.val);
                }
            } else {
                // 一层扫描完
                res.add(levelList);
                levelList = new LinkedList<>();
                // 下一层添加分界
                if (queue.size() > 0)
                    queue.addLast(null);
                
                isReverse = !isReverse;
            }
        }

        return res;
    }


    // DFS解法
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if (root == null) return new ArrayList<List<Integer>>();

        List<List<Integer>> res = new ArrayList<List<Integer>>();
        dfs(root, 0, res);
        return res;
    }

    private void dfs(TreeNode node, int level, List<List<Integer>> res) {
        if (node == null) return;

        // 需要扩张
        if (level == res.size()) {
            LinkedList<Integer> newLevel = new LinkedList<>();
            res.add(newLevel);
        }

        if (level % 2 == 0) {
            res.get(level).add(node.val);
        } else {
            res.get(level).add(0, node.val);
        }

        if (node.left != null) dfs(node.left, level + 1, res);
        if (node.right != null) dfs(node.right, level + 1, res);
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