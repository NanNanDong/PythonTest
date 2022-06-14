import java.util.HashMap;
import java.util.HashSet;

public class J160 {
    
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public class Solution {
        public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
            HashSet<ListNode> set = new HashSet<>();
            
            ListNode cur = headA;
            while (cur != null) {
                set.add(cur);
                cur = cur.next;
            }
            
            cur = headB;
            while (cur != null) {
                if (set.contains(cur)){
                    return cur;
                }
                cur = cur.next;
            }
            return null;
        }
    }
}
