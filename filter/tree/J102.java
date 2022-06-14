package filter.tree;

import java.util.List;

// 层序遍历是 队列 相关

// dfs也可以解：传入level

public class J102 {
    

    class Solution {
        public List<List<Integer>> levelOrder(TreeNode root) {
    
        }

        public void bfs(){

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
