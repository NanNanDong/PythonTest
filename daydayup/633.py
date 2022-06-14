# 633. 平方数之和

# 双指针
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low, high = 0, int(c**0.5)
        while low<=high:
            sumOf = low*low+high*high
            if sumOf==c: return True
            elif sumOf<c: low += 1
            else: high -= 1
        return False





