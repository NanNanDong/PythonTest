# 781. 森林中的兔子

# https://leetcode-cn.com/problems/rabbits-in-forest/solution/gong-shui-san-xie-noxiang-xin-ke-xue-xi-v17p5/
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()

        i, res, n = 0, 0, len(answers)

        while i < n:
            cur = answers[i]
            res += (cur + 1)

            while cur > 0 and i + 1 < len(answers) and answers[i] == answers[i + 1]:
                cur -= 1
                i += 1
            i += 1
        
        return res

