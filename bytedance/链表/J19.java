public class J19 {

    // 19. 删除链表的倒数第 N 个结点

  public class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }
 
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode fast = head, slow = dummy; // 从其前面开始 ！！！！

        // fast先走n+1步
        for (int i = 0; i < n; i++) {
            fast = fast.next;
        }

        if (slow == fast)
            return head;

        // 移动指针，找到slow前一个，所以fast为空则返回
        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }

        slow.next = slow.next.next;
        return dummy.next;
    }
}
    
}
