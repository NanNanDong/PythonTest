# 17. 电话号码的字母组合

# 回溯 DFS
# 当题目中出现 “所有组合” 等类似字眼时，我们第一感觉就要想到用回溯。

# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/pythondian-hua-hao-ma-de-zi-mu-zu-he-by-jutraman/

# BFS 很快

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = [] # 输出结果
        def dfs(index: int, digits: str, s: str):
            # 递归终止条件
            if index == len(digits):
                res.append(s)
                return
            
            digit = digits[index] # 当前数字
            vals = phoneMap[digit] # 当前数字对应的字母

            for i in range(len(vals)):
                dfs(index + 1, digits, s + vals[i]) # 递归去找下一个
            
        dfs(0, digits, "")

        return res



    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # BFS
        deque = collections.deque()
        deque.append("")

        for i in range(len(digits)): # 遍历所有数字
            lens_deque = len(deque) 
            for j in range(lens_deque): # 弹出所有队列内的数据，append末尾进行组合
                vals = phoneMap[digits[i]]
                cur_deque_vals = deque.popleft()
                for digit in vals:
                    deque.append(cur_deque_vals + digit)
                
            # print("当前队列中的内容：",deque)  ##这一句就一下明白每次在干啥了
        
        return list(deque)





