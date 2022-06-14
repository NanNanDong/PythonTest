import java.util.HashMap;
import java.util.Map;

class Solution {

    // 从前中序列 构造二叉树
    // 假设树中没有重复的元素

    // 前：[ 根节点, [左子树的前序遍历结果], [右子树的前序遍历结果] ]
    // 中：[ [左子树的中序遍历结果], 根节点, [右子树的中序遍历结果] ]
    // 可以得到根节点，根据其在中序遍历序列(需要用到边界，所以要传入边界递归)
    // 根据左子树的数量相等，得到前序遍历序列左子树和右子树的边界值 ！！！
    // 优化：因为要反复拿中序遍历的node对应的index，所以用map存一下(假设树中没有重复的元素)

    // 递归终止条件：边界不构成区间
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // 判断长度是否相等

        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            map.put(inorder[i], i);
        }
        // 这里怎么和递归函数联系？
        return build(preorder, 0, preorder.length-1, 0, inorder.length-1, map);
    }

    // preLeft:前序遍历子区间的左边界
    // preRight:前序遍历子区间的右边界
    // inLeft:中序遍历子区间的左边界
    // inRight:中序遍历子区间的右边界
    // 上述都不区分左右，构造时体现(都是闭区间)
    private TreeNode build(int[] preorder, int preLeft, int preRight, int inLeft, int inRight,
            Map<Integer, Integer> map) {
        if (preLeft > preRight || inLeft > inRight) {
            return null;
        }

        // 根据前序的第一个构造根节点
        int rootVal = preorder[preLeft];
        TreeNode root = new TreeNode(rootVal);
        int pIndex = map.get(rootVal); // 中序遍历的根节点位置

        // 核心是这里，得在草稿纸上算！！！！
        // 左子树的边界
        root.left = build(preorder, preLeft + 1, pIndex - inLeft + preLeft, inLeft, pIndex - 1, map); 
        // 
        root.right = build(preorder, pIndex-inLeft+preLeft+1, preRight, pIndex+1, inRight, map);
        return root;

    }

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }
}