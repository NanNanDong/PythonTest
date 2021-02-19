# 1128. 等价多米诺骨牌对的数量
# 二元组表示：因为均不大于9，可以用10进制表示，相当于特殊的Hash了

from typing import List
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
        pairDict = dict()
        for x, y in dominoes:
            num = (x * 10 + y if x <= y else y * 10 + x)
            if num in pairDict:
                pairDict[num] = pairDict[num] + 1
                count += pairDict[num]
                # pairSet.remove(num)
            else:
                pairDict[num] = 0
        
        return count

x = Solution()
print(x.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))

print(x.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))
