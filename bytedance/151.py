# 151. 翻转字符串里的单词

# 1. 利用系统函数
# 2. 利用栈/双端队列
# 3. 先翻转字符串，再翻转单词(C++不用单独实现)
class Solution:
    def reverseWords1(self, s: str) -> str:
        return " ".join(reversed(s.split()))


    # 自己实现函数
    def trimSpaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1
        # 去掉末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1

        print(left, " --> ", right)
        
        # 去掉字符之间多余的空白字符
        output = [] # 这就不是O(1)了吧
        while left <= right:
            if s[left] != ' ':
                output.append(s[left]) # 一位位往后读
            elif output[-1] != ' ': # 添加一个空格
                # print(output[-1], "----->", s[left])
                output.append(s[left])
            left += 1 # 跳过多余的
        return output

    # 翻转一个List字符串，left到right部分 ---> 不用返回值
    def reverse(self, l: list, left: int, right: int):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    # 翻转所有字符
    def reverseEachWord(self, l: list):
        n = len(l)
        start = end = 0

        while start < n:
            # 循环至单词的末尾，得出单词长度
            while end < n and l[end] != ' ':
                end += 1
            # 翻转单词
            self.reverse(l, start, end - 1)
            # 更新start，去找下一个单词
            start = end + 1
            end += 1
            
    def reverseWords(self, s: str) -> str:
        l = self.trimSpaces(s) # 去除多余空格
        print(l)
        # 翻转字符串
        self.reverse(l, 0, len(l) - 1)
        # 翻转每个单词
        self.reverseEachWord(l)

        return ''.join(l)

x = Solution()
print(x.reverseWords("the sky is blue"))
print(x.reverseWords("  hello world  "))

