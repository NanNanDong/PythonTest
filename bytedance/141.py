# 141. 环形链表
# 1.哈希表
# 2.快慢指针

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
    
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next: # 快指针跑到尾了
                return False
            slow = slow.next
            fast = fast.next.next

        return True
