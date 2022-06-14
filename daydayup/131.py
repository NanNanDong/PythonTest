# 131. 分割回文串

# dfs递归回溯，动态规划的状态太多(不好理)


from typing import List


class Solution:
    
    def partition(self, s: str) -> List[List[str]]:
        # 辅助函数，判断当前子串是否是回文串
        
        @cache
        def isPalindrome(substring):
            if substring == substring[::-1]: return True
            else: return False

        res = []
        
        # 判断本身是否是空串
        if not s: return res

        #remain表示除了已经找到回文子串余下的子串
        def dfs(remian, tmp):
            # print('>> ', remian, ',', tmp)
            if len(remian) == 0: #剩下的子串都找完了，且都是回文串，并入最终res中
                res.append(tmp)
            for i in range(len(remian)): #每次从剩下的子串中，分成左右两个部分，不断划分，直到左边部分是回文串才进入下一次回溯
                left = remian[:i+1]
                right = remian[i+1:]
                if isPalindrome(left): #左边部分是回文串，并入tmp中，把右边部分当做remain，进入下一次回溯
                    # print('--> ',tmp, ',', [left])
                    dfs(right, tmp+[left])
                else:
                    continue
        dfs(s, [])
        return res

x = Solution()
print(x.partition("aab"))