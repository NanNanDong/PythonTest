# 438. 找到字符串中所有字母异位词

from typing import List


class Solution:
    # 滑动窗口 + 数组
    def findAnagrams1(self, s: str, p: str) -> List[int]:
        n, m, res = len(s), len(p), []
        if n < m: return res
        
        s_cnt = [0] * 26
        p_cnt = [0] * 26

        
        # 预处理
        for i in range(m):
            s_cnt[ord(s[i]) - ord('a')] += 1
            p_cnt[ord(p[i]) - ord('a')] += 1 # 更新匹配count数组

        if s_cnt == p_cnt:
            res.append(0)

        for i in range(m, n):
            s_cnt[ord(s[i - m]) - ord('a')] -= 1 # 左边的移出
            s_cnt[ord(s[i]) - ord('a')] += 1 # 右边的移进来

            if s_cnt == p_cnt:
                res.append(i - m + 1)
        
        return res

    # 滑动窗口 + 双指针
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m, res = len(s), len(p), []
        if n < m: return res

        s_cnt = [0] * 26
        p_cnt = [0] * 26

        for i in range(m):
            p_cnt[ord(p[i]) - ord('a')] += 1

        left = 0
        # 右移动 右指针
        for right in range(n):
            cur_right = ord(s[right]) - ord('a')
            s_cnt[cur_right] += 1
            
            # 因为添加进来一个右边的字符
            # 右移左指针，直到 条件不符合
            while s_cnt[cur_right] > p_cnt[cur_right]:
                cur_left = ord(s[left]) - ord('a') # 头脑要清楚，这里移动左指针，要更新左指针的值
                s_cnt[cur_left] -= 1
                left += 1 # 左指针右移
            
            if right - left + 1 == m: # 符合条件
                res.append(left)
            
        return res

