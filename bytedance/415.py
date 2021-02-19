# 415. 字符串相加

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0: # 字符串长短操作
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[i]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10 # 进位操作
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res

x = Solution()
# print(x.addStrings("199", "3211"))
print(x.addStrings("1", "9"))
print(x.addStrings("1", "7"))
print(x.addStrings("4", "9"))

        
