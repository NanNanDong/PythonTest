# 82. 删除排序链表中的重复元素 II

# 排序列表

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        dummyHead = ListNode(-1)
        dummyHead.next = head

        a = dummyHead
        b = head

        # 后面的指针没遍历到结尾，如果b没有指向了，也就提前结束了(需要体会)
        while b and b.next:
            # 画图知道，a、b的指向不同时，才能往下跳一步
            if a.next.val != b.next.val:
                a = a.next
                b = b.next
            else:
                # 如果a、b的指向相同，就不断移动b，直到不相等
                while b and b.next and a.next.val == b.next.val:
                    b = b.next
                a.next = b.next # a跨越山河指向b的指向(这一步需要体会，不是指向b)
                b = b.next

        return dummyHead.next

    # hashmap存储下频率，好写一些
    def deleteDuplicates1(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        d = dict()
        p = head
        arr = []

        while p:
            val = p.val
            d[val] = d.setdefault(val, 0) + 1 # python大法好
            p = p.next

        # 将所有只出现一次的放入arr
        for k in d:
            if d[k] == 1:
                arr.append(k)
        arr = sorted(arr) # 哈希表可能会更改顺序

        dummyHead = ListNode(-1)
        p = dummyHead
        # 把arr的值赋予arr
        for i in arr:
            tmp = ListNode(i)
            p.next = tmp
            p = p.next
        
        return dummyHead.next





