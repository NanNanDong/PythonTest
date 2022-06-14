# 61. 旋转链表

# https://leetcode-cn.com/problems/rotate-list/solution/fu-xue-ming-zhu-wen-ti-chai-fen-fen-xian-z4dr/

# 1. 快慢指针
# 2. 闭合成环


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head

        # 链表长度
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        # 对长度取模
        k %= n
        if k == 0: return head

        # 让fast先走k步
        fast, slow = head, head
        while k :
            fast = fast.next
            k -= 1

        # 当fast为空，fast指向链表最后一个节点，slow指向倒数k+1个
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # newHead是倒数第k个节点，即新链表当头
        newHead = slow.next
        # 让最后一个节点断开，原先最后一个节点指向原链表当头
        slow.next = None
        fast.next = head

        return newHead


    # 闭合成环，再断开
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0: return head

        # 计算数组长度
        cnt, t = 0, head

        while t.next:
            t = t.next
            cnt += 1

        cnt += 1
        k %= cnt

        t.next = head

        # 找到新的头节点的前一个节点
        k = cnt - k - 1
        while k > 0:
            head = head.next
            k -= 1
        
        res = head.next 
        head.next = None # 断开

        return res



        



