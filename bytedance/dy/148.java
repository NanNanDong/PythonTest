// 148. 排序链表

// 归并排序（时间辅助度推出） + 递归
// 归并找中点：快慢指针
// 辅助函数：合并两个链表
 
class Solution {
    public ListNode sortList(ListNode head) {
        return mergeSort(head, null);
    }

    public ListNode mergeSort(ListNode start, ListNode end) {
        if (start == end) return null;
        // 快慢指针找中点
        ListNode fast = start, slow = start;
        // fast不能等于endend 
        while (start != end && fast.next != end) {
            fast = fast.next.next;
            slow = slow.next;
        }

        // 后面的点要断，但后一截要用，所以先得到l2
        ListNode l2 = mergeSort(slow.next, end);
        slow.next = null;
        ListNode l1 = mergeSort(start, slow);
        
        return merge(l1, l2); // 合并链表
     }

     // 合并两个子链表，子链表有序，但并不是直接拼到后面，要遍历
     public ListNode merge(ListNode l1, ListNode l2) {
         if (l1 == null) return l2;
         if (l2 == null) return l1;

         if (l1.val < l2.val) { 
             // l1比较小，排序后的插到l1后面
             l1.next = merge(l1.next, l2);
             return l1;
         } else {
             l2.next = merge(l1, l2.next);
             return l2;
         }
     }

    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
}