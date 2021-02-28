# 2. 两数相加
# 不要想的太多，就是while，是有个长短字符的取巧解法，但这里没必要

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0 # 有进位好理解些，可以和sum合并
        sum = 0
        dummpy = p = ListNode(0)

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1 + v2 + carry
            p.next = ListNode(sum % 10)
            p = p.next
            carry = 1 if sum >= 10 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry:
            p.next = ListNode(1)
        
        return dummpy.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def dfs(v1: ListNode, v2: ListNode, carry: int) -> ListNode:
            if not v1 and not v2 and not carry: return None
            sum = (v1.val if v1 else 0) + (v2.val if v2 else 0) + carry
            node = ListNode(sum % 10)
            node.next = dfs(v1.next if v1 else None, v2.next if v2 else None, sum // 10)
            return node
        
        return dfs(l1, l2, 0)

    



