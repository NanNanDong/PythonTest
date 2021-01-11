# 21. 合并两个有序链表
# 1. 迭代：dummyHead、链表赋值、res更新、结尾
# 2. 递归
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(-1) # 使用 dummyHead 返回

        res = dummyHead
        while l1 and l2:
            if l1.val <= l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next # 存储的链表也要更新
        
        if l1:
            res.next = l1
        elif l2:
            res.next = l2
        
        return dummyHead.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        elif l2 is None: return l1
        elif l1.val < l2.val: # 递归进来，后面会回溯回去的
            l1.next = self.mergeTwoLists(l1.next, l2) 
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

