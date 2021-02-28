# 142. 环形链表 II

# 链表有环问题
# 1.哈希表； 2.快慢指针


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head

