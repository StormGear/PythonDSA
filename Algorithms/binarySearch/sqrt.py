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
                
# print(Solution().mySqrt(16))

# another approach
class Solution:
    def compute_sqrt(self, x: float) -> float:
        """
        Compute the square root of a number using binary search
        Args:
            x: The number to find square root of
        Returns:
            The square root with precision up to 6 decimal places
        """
        if x < 0:
            raise ValueError("Cannot compute square root of negative number")
        if x == 0 or x == 1:
            return x
        
        # For integer part
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        
        # For decimal part (precision up to 6 decimal places)
        increment = 0.1
        for _ in range(6):
            while ans * ans <= x:
                ans += increment
            ans -= increment
            increment /= 10
        
        return round(ans, 6)
    
if __name__ == "__main__":
    sqrt = Solution()
    print(sqrt.compute_sqrt(8)) # 2.828427
    

    


    