# 832. 翻转图像

# 因为我们是同时修改了左右对称的元素，所以我们只用遍历到每一行的中间位置


from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        N = len(A)
        for i in range(N):
            for j in range((N + 1)//2):
                A[i][j], A[i][N - 1- j] = 1 - A[i][N - 1 -j], 1- A[i][j]
        return A

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        rows = len(A)
        cols = len(A[0])
        for row in range(rows):
            A[row] = A[row][::-1]
            for col in range(cols):
                A[row][col] ^= 1
        return A



