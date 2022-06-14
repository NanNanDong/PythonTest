# 92. 反转链表 II

# 反转从位置 m 到 n 的链表
# 206: https://leetcode-cn.com/problems/reverse-linked-list/solution/206-fan-zhuan-lian-biao-shuang-zhi-zhen-o472f/

# 思路1 细节较多，但思维较容易从206扩展而来，就是翻转 [m-n] 后，把断开的前后部分接上去(拉直)
# 思路2 比较巧妙，保持第一个翻转的位置不变，不断把需要翻转的元素扔到该位置
# https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/fan-zhuan-lian-biao-ii-by-leetcode-solut-teyq/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head

        pre = dummyHead
        for _ in range(m - 1):
            pre = pre.next

        cur = pre.next

        for _ in range(m - n):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        
        return dummyHead.next
