# 91. 解码方法
# 暴力：1.对于任何一个字符串，我们每次可以读取一到两个；2.set存储合法数值
# 递归L：难点 s[i] s[i-1]+s[i] 分开讨论

# https://leetcode-cn.com/problems/decode-ways/solution/gong-shui-san-xie-gen-ju-shu-ju-fan-wei-ug3dd/
class Solution:
    def numDecodings(self, s: str) -> int:

