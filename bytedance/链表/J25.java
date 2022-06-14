/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0, head); // 肯定要dummy存的，因为返回的格式

        ListNode prev = dummy; // prev每次指向要反转的链表的头节点的上一个节点
        ListNode end = dummy; // end每次指向要反转的链表的尾节点

        while (end != null) {
            // 判断k的大小
            for (int i = 0; i < k && end != null; i++) {
                end = end.next;
            }
            if (end == null) break; // 不需要反转

            // 记录下end.next，便于后面连接链表
            ListNode next = end.next;
            end.next = null; // 断开链表，顺便让辅助函数好写了

            // 记录下要反转的头节点
            ListNode start = prev.next;

            // 反转链表，并连接到prev
            prev.next = reversNodes(start); 

            // 反转后，头节点变到最后面了，与之前断开的连接
            start.next = next;

            // 维护prev和end，继续下一次反转
            prev = start;
            end = start;
        }

        return dummy.next;
    }

    private ListNode reversNodes(ListNode head) {
        ListNode prev = null;
        ListNode cur = head;

        while (cur != null) {
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }
}