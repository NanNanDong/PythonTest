# 995. K 连续位的最小翻转次数
# 一次K位翻转
# 思路有点难的
from typing import List
import collections
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        que = collections.deque()
        res = 0
        for i in range(n):
            if que and i >= que[0] + K:
                que.popleft()

            # 当 i 位置被翻转了偶数次，如果 A[i] 为 0，那么翻转后仍是 0，当前元素需要翻转；
            # 当 i 位置被翻转了奇数次，如果 A[i] 为 1，那么翻转后是 0，当前元素需要翻转。
            # ---> len(que) % 2 == A[i]
            if len(que) % 2 == A[i]:
                if i + K > n: return -1 # 后面剩余的元素不到 K 个了
                que.append(i)
                res += 1
        return res


