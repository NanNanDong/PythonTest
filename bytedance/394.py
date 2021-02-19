# 394. 字符串解码
# 1.递归+模式匹配！！！每个子括号对应一个子问题 ---> 不太常规
# 2.利用栈，从前往后，逻辑更清晰
class Solution:
    def decodeString1(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                # 将当前 multi 和 res 入栈，并分别置空置为0
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                # 拼接字符串
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res



x = Solution()
print(x.decodeString("3[a]2[bc]"))
print(x.decodeString("3[a2[c]]"))
print(x.decodeString("2[abc]3[cd]ef"))
print(x.decodeString("abc3[cd]xyz"))