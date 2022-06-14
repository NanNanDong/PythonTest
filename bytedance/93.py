# 93. 复原 IP 地址

# 回溯
# 递归函数 dfs(segId,segStart) 
# 表示我们正在从 s[segStart] 的位置开始，搜索 IP 地址中的第 segId 段

# https://leetcode-cn.com/problems/restore-ip-addresses/solution/fu-yuan-ipdi-zhi-by-leetcode-solution/
# https://leetcode-cn.com/problems/restore-ip-addresses/solution/hui-su-suan-fa-hua-tu-fen-xi-jian-zhi-tiao-jian-by/

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

