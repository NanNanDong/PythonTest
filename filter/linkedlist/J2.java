package filter.linkedlist;

// 重点在长短

public class J2 {

    class Solution {
        public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
            ListNode res = new ListNode(0);
            ListNode dummy = res;

            int acc = 0;
            
            while (l1 != null || l2 != null) {
                int n1 = l1 != null ? l1.val : 0;
                int n2 = l2 != null ? l2.val : 0;

                int sum = n1 + n2 + acc;

                if (sum >= 10) {
                    sum = sum - 10;
                    acc = 1;
                } else {
                    acc = 0;
                }

                res.next = new ListNode(sum);
                res = res.next;

                // 是l1不是l1的next不为空
                if (l1 != null) l1 = l1.next;
                if (l2 != null) l2 = l2.next;
            }

            // 最后要处理下进位
            if (acc == 1) {
                res.next = new ListNode(1);
            }

            return dummy.next;

        }

        public class ListNode {
            int val;
            ListNode next;

            ListNode() {
            }

            ListNode(int val) {
                this.val = val;
            }

            ListNode(int val, ListNode next) {
                this.val = val;
                this.next = next;
            }
        }

    }

}
