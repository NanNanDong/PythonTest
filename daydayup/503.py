# 503. 下一个更大元素 II

from typing import List


class Solution:
    # 暴力
    def nextGreaterElements1(self, nums: List[int]) -> List[int]:
        res = list()
        tmp = nums + nums
        n = len(nums)

        for i in range(n):
            j = i
            val = nums[i]
            while j <= (2 * n - 1):
                if tmp[j] > val:
                    res.append(tmp[j])
                    break
                j += 1
                if (j == 2*n-1):
                    res.append(-1)
        return res

    # 单调栈
    # 保持一个非递增的，遇到不符合能递增的，则将栈内的pop出来，nums[i]就是其对应元素
    # 因为不符合的，在之前就被处理了
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        decStack = list()
        n = len(nums)
        res = [-1] * n
        for i in range(2 * n - 1):
            # 栈非空，判断条件 出栈比较 栈顶索引 对应元素值与当前元素值的大小
            while decStack and nums[decStack[-1]] < nums[i % n]: 
                res[decStack.pop()] = nums[i % n]
            # 压入栈中的是元素的索引
            # 这里用取模的方法映射索引到原数组中
            decStack.append(i % n)

        return res

                


x = Solution()
print(x.nextGreaterElements([1, 2, 1]))

