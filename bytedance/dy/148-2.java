
// 排序奇升偶降链表

// 1.分割成两个链表
// 2.再逆序偶链表
// 3.合并两个有序链表

class Solution {
    public ListNode sortList(ListNode head) {
        return mergeSort(head, null);
    }

    // 分拆链表
    public ListNode splitAndMerge(ListNode head) {
        ListNode dummy1 = new ListNode();
        ListNode dummy2 = new ListNode();
        ListNode l1 = dummy1, l2 = dummy2;
        boolean flag = true;
        ListNode cur = head;
        while (cur != null) {
            if (flag) {
                l1.next = cur;
                l1 = l1.next;
            } else {
                l2.next = cur;
                l2 = l2.next;
            }
        }

        // 翻转l2
        l2 = reverse(l2);
        // 拼接
        return mergeSort(l1, l2);
    }

    // 翻转链表
    public ListNode reverse(ListNode head) {
        if (head == null) return null;
        ListNode cur = head;
        ListNode pre = null;
        while (cur.next != null) {
            ListNode next = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next;
        }
        return pre;
    }

    // 归并一个链表
    public ListNode mergeSort(ListNode start, ListNode end) {
        if (start == end) return null;
        ListNode fast = start, slow = start;
        // 找
        while (fast != end && fast.next != end) {
            fast = fast.next.next;
            slow = slow.next;
        }
        // 分
        ListNode l2 = mergeSort(slow.next, end);
        slow.next = null;
        ListNode l1 = mergeSort(start, slow);
        // 合
        return merge(l1, l2);

    }

    public ListNode merge(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;

        if (l1.val < l2.val) { // l1比较小
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
