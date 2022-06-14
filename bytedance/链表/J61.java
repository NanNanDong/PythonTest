public class J61 {

    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    
    class Solution {
        public ListNode rotateRight(ListNode head, int k) {
            // 组成环剪断，关键是这个head得想清楚 (和19题一样可以快慢指针)
            // 先把答案头节点用newHead记住，然后断掉前继节点，这样就形成了答案链表
            if (head == null || k == 0) return head;

            int length = 0; // 总长度
            ListNode tail = head;
            while (tail.next != null) {
                tail = tail.next;
                length += 1;
            }

            length += 1; // 最后一个没加，长度为1模拟下就知道了

            // k 如果比 length 长 ！这个取余操作精髓
            k %= length;
            
            if (k == 0) return head;

            // 闭合成环
            tail.next = head;

            k = length - k - 1; // 找到需要断开的前一个
            while(k > 0) {
                k -= 1;
                head = head.next;
            }

            ListNode res = head.next;
            head.next = null;
            return res;
        }
    }

}
