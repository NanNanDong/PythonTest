# 81. 搜索旋转排序数组 II

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False

        n = len(nums)

        if n == 1: return nums[0] == target

        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2
            # 命中
            if nums[mid] == target: return True
            
            # 区分不了升降区间
            if nums[l] == nums[mid]:
                l += 1
                continue
            # 后半部分升序
            if nums[mid] <= nums[r]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # 前半部分有序
            else:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return False
            

x = Solution()
print(x.search([1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1], 13))



