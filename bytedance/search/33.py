# 33. 搜索旋转排序数组

# 有序或者部分有序，基本使用二分变种(每次丢弃一半数据)
# 怎么丢弃一半数据？
# 1.判断左右两边的端点，就可以判断是否有序
# 2.若在有序的一边，则在有序这边搜，否则去无序那边

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # 左半边有序
            if nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]: # 位于左半边
                    r = mid - 1
                else:
                    l = mid + 1
            # 右半边有序
            else:
                if nums[mid] <= target <= nums[r]: # 位于右半边
                    l = mid + 1
                else:
                    r = mid - 1
            
        return -1

x = Solution()
print(x.search([4,5,6,7,0,1,2], 0))

