# 79. 单词搜索

# 回溯 + 剪枝
# 想清楚了是有思路到，但是确实写着不简单
# https://leetcode-cn.com/problems/word-search/solution/shen-du-you-xian-sou-suo-yu-hui-su-xiang-jie-by-ja/

from typing import List


class Solution:

    # 定义上下左右四个方向
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def backtrack(self, i: int, j: int, mark: List[int], board: List[List[int]], word: str) -> bool:
        if len(word) == 0: return True

        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]

            if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                # 如果是已经使用过到元素，忽略
                if mark[cur_i][cur_j] == 1: continue

                # 将该元素标记为已使用
                mark[cur_i][cur_j] = 1

                # 往下查找
                if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
                    return True
                else:
                    mark[cur_i][cur_j] = 0 # 核心！回溯
        
        return False
                

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board) # 少算一点，可以借鉴
        if m == 0: return False

        n = len(board[0])

        mark = [[0 for _ in range(n)] for _ in range(m)]

        # 外层定位首字符
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    # 将该元素标记为已使用
                    mark[i][j] = 1
                    if self.backtrack(i, j, mark, board, word[1:]) == True:
                        return True
                    else:
                        mark[i][j] = 0 # 回溯
        
        return False


x = Solution()
print(x.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))    

