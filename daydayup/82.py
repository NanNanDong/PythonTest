# 82. 删除排序链表中的重复元素 II
# 是相同的都删掉

# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/solution/fu-xue-ming-zhu-di-gui-die-dai-yi-pian-t-wy0h/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head

        while cur:
            # 跳过当前的重复节点，使得cur指向当前重复元素的最后一个位置
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur:
                pre = pre.next
            else:
                # 删除重复的元素
                pre.next = cur.next
            cur = cur.next # 右指针移动

        return dummy.next

