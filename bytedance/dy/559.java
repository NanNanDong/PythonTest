// 559. N 叉树的最大深度

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public int maxDepth(Node root) {
        return depth(root);
    }

    public int depth(Node root) {
        if (root == null) {
            return depth;
        }
        
        int res = 0;
        for (Node n : root.children) {
            res = Math.max(res, depth(n));
        }
        return res + 1;
    }
}