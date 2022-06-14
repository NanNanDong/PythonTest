# 83. 删除排序链表中的重复元素

# 删除一个节点：cur.next = cur.next.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        
        cur = head
        while cur.next:
            if cur.val == next.val:
                cur.next = next.next
            else:
                cur = cur.next
        
        return head