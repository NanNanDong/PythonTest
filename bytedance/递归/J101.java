import apple.laf.JRSUIUtils.Tree;

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
    
   class Solution {
       public boolean isSymmetric(TreeNode root) {
           if (root == null) return true;

        //    return isSymmetric(root.left) && isSymmetric(root.right);  // 这个只能判断是否为空！
           return dfs(root.left, root.right); 
       }

       private boolean dfs(TreeNode left, TreeNode right) {
           if (left == null && right == null) return true;
           if (left == null || right == null) return false;

           if (left.val != right.val) return false;

           // 递归比较，画图理解(一般题上也有)，递归执行是左边的左边和右边的右边相等，左边的右边和右边的左边相等
           return dfs(left.left, right.right) && dfs(left.right, right.left);
       }
   }