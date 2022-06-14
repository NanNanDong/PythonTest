# 354. 俄罗斯套娃信封问题

# 一看就是最长上升子序列问题，很关键的提示信息：不允许旋转信封
# dp[i] = max(1, dp[j] + 1); //j > i and arr[j] < arr[i]

from typing import List


class Solution:
    def maxEnvelopes1(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        n = len(envelopes)
        # 信封按照 w 值第一关键字升序、h 值第二关键字降序进行排序
        # 排序后，忽略w维度，h求LIS
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        f = [1] * n
        for i in range(n):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]: 
                    f[i] = max(f[i], f[j] + 1)
        
        return max(f)

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes: return 0

        n = len(envelopes)
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        
        # 如果当前数字，比LIS的都大，就加在后面
        # 如果当前数字，在LIS是第pos大，那他就替代pos的位置，因为当前的更小，更有利于后面的比pos位置的大
        LIS = [envelopes[0][1]]
        for i in range(1, n):
            pos = bisect.bisect_left(LIS, envelopes[i][1])
            if pos == len(LIS):
                LIS.append(envelopes[i][1])
            else:
                LIS[pos] = envelopes[i][1]
        
        return len(LIS)



    

envelopes = [[5,4],[6,4],[6,7],[2,3]]
envelopes.sort(key=lambda x: (x[0], -x[1]))
print(envelopes)

if (num := 3) < 2: print("YES")
else: print("NO")