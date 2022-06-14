# 220. 存在重复元素 III
# 1.桶排序，假如k=5，则[0,5]为第0个桶，[6,11]为第1个桶，[12,17]为第2个桶，[-6,-1]为第-1个桶
# 2.检查桶内以及相邻的即可
# 3.精髓在getIdx的思路：

from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # 获取桶序号 ########
        def getIdx(u: int) -> int:
            return (u + 1) // size - 1 if u < 0 else u // size
        
        size = t + 1
        map = {} # 存储的是

        for i, u in enumerate(nums):
            idx = getIdx(u)
            # print(idx)
            # 目标桶已存在（桶不为空），说明前面已有 [u - t, u + t] 范围的数字
            if idx in map:
                return True # 同一桶内查找成功
            # 查找相邻的桶
            l, r = idx - 1, idx + 1
            if l in map and abs(u - map[l]) <= t:
                return True
            if r in map and abs(u - map[r]) <= t:
                return True
            # 建立目标桶
            map[idx] = u
            # print(map)
            # 维护个数为k
            if i >= k:
                # print(nums[i - k], getIdx(nums[i - k]))
                map.pop(getIdx(nums[i - k]))

        return False

       

x = Solution()
print(x.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
# print(x.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2))
# print(x.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))
# print(x.containsNearbyAlmostDuplicate([1,2,2,3,4,5],3, 0))
            
            

