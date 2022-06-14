// K 个一组翻转链表

class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0, head); // 按照返回的格式肯定要dummy
        
        // 最大思维点
        ListNode prev = dummy; // 每次指向要翻转链表的头节点的上一个(hair)
        ListNode end = dummy; // 每次指向要翻转链表的尾节点，初始化与prev相同

        while (end != null) {
            // 判断k的大小，移动end
            for (int i = 0; i < k && end != null; i++) {
                end = end.next;
            }
            if (end == null) break; // 不需要翻转

            // 记录下end.next，后面拼回去要用
            ListNode next = end.next;
            end.next = null; // 置为null，不然辅助函数不终止

            // 记录要翻转的头节点
            ListNode start = prev.next;

            // 翻转链表，拼接到prev
            prev.next = reverseList(start);

            // 翻转后，头节点变到后面了，通过其next与之前存储的end的next连接
            start.next = next;

            // 维护prev和end，继续下一次翻转
            prev = start;
            end = start;
        }
 
        return dummy.next;
    }

    // 辅助函数，翻转链表
    public ListNode reverseList(ListNode head) {
        if (head == null) return null;
        ListNode cur = head;
        ListNode prev = null;
        while (cur != null) {
            ListNode next = head.next; // 暂存
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }

  public class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }
}