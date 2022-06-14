# 1047. 删除字符串中的所有相邻重复项

# 利用栈，用啥指针

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stk = list()
        for ch in S:
            if stk and stk[-1] == ch:
                stk.pop()
            else:
                stk.append(ch)

        return "".join(stk)


s = "hello"
print(s[0])            