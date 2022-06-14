# 315. 计算右侧小于当前元素的个数

from typing import List

# 1.归并排序，索引数组
# 2.树状数组是用数组来模拟树形结构，可以解决大部分基于区间上的更新以及求和问题。树状数组中修改和查询的复杂度都是O(logN)

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:


