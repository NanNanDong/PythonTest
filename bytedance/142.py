# 142. 环形链表 II

# 链表有环问题 - 141 返回判断结果，这题需要返回pos
# 1.哈希表； 2.快慢指针
# 小技巧：如果数据可修改，可以原地修改，如果遍历的时候发现是修改过的，则有环

# 求 pos： 画图，分三段，任意时刻，fast 指针走过的距离都为 slow 指针的 2 倍
# a+(n+1)b+nc=2(a+b)  ⟹  a=c+(n−1)(b+c)
# 从相遇点到入环点的距离加上 n-1n−1 圈的环长，恰好等于从链表头部到入环点的距离

# 所以，相遇后，将一个节点放到链表头部，另一个继续从相遇处，每次移动一步，最终会在入环点相遇

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head

        # 快慢指针，快指针如果走得到头，那肯定没环
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: break
        
        if not fast or not fast.next: return None

        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast

