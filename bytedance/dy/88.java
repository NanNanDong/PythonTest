// 88. 合并两个有序数组

// 比归并少个数组的空间复杂度
// 逆向双指针，nums1后半段为空，避免元素取出前被覆盖
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m - 1, p2 = n - 1;
        int tail = m + n - 1;
        int cur; // 当前数字

        while (p1 >= 0 || p2 >= 0) {
            if (p1 == -1) {
                cur = nums2[p2--];
            } else if (p2 == -1) {
                cur = nums1[p1--]; // 减号在后面，后减
            } else if (nums1[p1] > nums2[p2]) {
                cur = nums1[p1];
                p1 -= 1;
            } else {
                cur = nums2[p2];
                p2 -= 1;
            }
            nums1[tail--] = cur;
        }

    }

   
}