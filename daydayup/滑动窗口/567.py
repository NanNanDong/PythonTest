# 和76相同
# 字符出现的种类和次数相等
# 滑动过程(交替滑动)：
# 1.右指针不断往右，到s2满足包含s1的元素种类和个数；
# 2.左指针往右移，直到s2不满足包含s1的元素种类和个数，之前停止
# 数据结构设计：两个feq的数组、一个pCount:s1中出现的元素个数、1个winCount:某个字符出现的次数恰好相等
# 返回：pCount==winCount时，right-left

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pLen, winLen = len(s1), len(s2)
        pFeq, winFeq = [0] * 26, [0] * 26 # 千万不能去连续赋值，两个数组会联动
        left, right = 0, 0
        pCount, winCount = 0, 0

        for c in s1:
            # print(ord(c) - ord('a'))
            pFeq[ord(c) - ord('a')] += 1

        # 计算s1字符出现的频次
        for i in range(26):
            if pFeq[i] > 0: 
                pCount += 1

        # print('pCount = ', pCount)
        
        # 当滑动窗口中的某个字符个数与 s1 中对应相等的时候才计数
        while right < winLen:
            rightPos = ord(s2[right]) - ord('a')
            # print(rightPos)
            if pFeq[rightPos] > 0:
                winFeq[rightPos] += 1
                if winFeq[rightPos] == pFeq[rightPos]:
                    winCount += 1
            right += 1

            while pCount == winCount: # 因为可能重复进入
                if right - left == pLen:
                    # print("find -> [", left, ",", right, "], " , s2[left], s2[right])
                    return True
                
                leftPos = ord(s2[left]) - ord('a')
                if pFeq[leftPos] > 0:
                    winFeq[leftPos] -= 1
                    if winFeq[leftPos] < pFeq[leftPos]: # 把之前加的减回去
                        winCount -= 1
                left += 1

        return False

            
x = Solution()
# print(x.checkInclusion("ab", "eidbaooo"))
print(x.checkInclusion("ab", "eidboaoo"))






