# 头插法
# 分别称之为 g(guard 守卫) 和 p(point)
# 将 g 移动到第一个要反转的节点的前面，将 p 移动到第一个要反转的节点的位置上
# 将 p 后面的元素删除，然后添加到 g 的后面

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head

        g = dummyHead
        for _ in range(m - 1):
            g = g.next

        p = g.next

        for _ in range(n - m):
            removed = p.next # p的下一个需要删除
            p.next = p.next.next # 往下跳一格
            # 巧妙点
            removed.next = g.next # 插入到g的后面前，先把尾巴接过来
            g.next = removed

        return dummyHead.next