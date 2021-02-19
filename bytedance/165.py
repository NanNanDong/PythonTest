# 165. 比较版本号
# 这题感觉不像算法题啊
class Solution:
    def compareVersion1(self, version1: str, version2: str) -> int:
        v1s = version1.split('.')
        v2s = version2.split('.')
        lenV1 = len(v1s)
        lenV2 = len(v2s)
        maxx = max(lenV1, lenV2)

        for i in range(maxx):
            if i >= lenV1:
                if int(v2s[i]) > 0: return -1
            elif i >= lenV2: 
                if int(v1s[i]) > 0: return 1
            else:
                if int(v1s[i]) < int(v2s[i]): return -1
                elif int(v1s[i]) > int(v2s[i]): return 1

        return 0

    # 确实是别人写的火候好啊
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        n1, n2 = len(nums1), len(nums2)

        for i in range(max(n1, n2)):
            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1
        
        return 0




x = Solution()
print(x.compareVersion("1.01", "1.001"))
print(x.compareVersion("7.5.2.4", "7.5.3"))
print(x.compareVersion("1.0.1", "1"))
print(x.compareVersion("0.1", "1.1"))
