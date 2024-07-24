class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
                
print(Solution().mySqrt(4))

# another approach
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left + right)//2

            if mid*mid == x:
                return mid
            if mid*mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right