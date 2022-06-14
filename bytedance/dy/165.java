// 比较版本号

class Solution1 {
    public int compareVersion(String version1, String version2) {
        String[] nums1 = version1.split("\\.");
        String[] nums2 = version2.split("\\.");

        int len1 = nums1.length, len2 = nums2.length;
        int i1 = 0, i2 = 0;
        // for 循环的话取也是取大的
        while (i1 < len1 || i2 < len2) {
            int n1 = i1 < len1 ? Integer.parseInt(nums1[i1]) : 0;
            int n2 = i2 < len2 ? Integer.parseInt(nums2[i2]) : 0;
            if (n1 != n2) {
                return n1 - n2 > 0 ? 1 : -1;
            }
            i1++;
            i2++;
        }
        return 0;
    }


}