from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r] # max height on the left and right

        
        while l < r:
            if left_max < right_max: # left_max becomes the min of the two(right and left side)
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]

        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([0,2,0,3,1,0,1,3,2,1]))  # Output: 9