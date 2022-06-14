# 20. 有效的括号

class Solution:
    def isValid1(self, s: str) -> bool:
        stk = []

        for ch in s:
            if ch in '({[':
                stk.append(ch)
                continue

            if ch == ')' and (not stk or stk.pop() != '('):
                return False
            elif ch == '}' and (not stk or stk.pop() != '{'):
                return False
            elif ch == ']' and (not stk or stk.pop() != '['):
                return False

        return len(stk) == 0

    def isValid(self, s: str) -> bool:
        pairs = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stk = list()

        for ch in s:
            if ch in pairs:
                if not stk or stk.pop() != pairs[ch]:
                    return False
            else:
                stk.append(ch)
        
        return not stk
    

x = Solution()
# print(x.isValid("()"))
# print(x.isValid("()[]{}"))
# print(x.isValid("(]"))
# print(x.isValid("([)]"))
print(x.isValid("]"))