# Smallest distance pair

# 719. Find K-th Smallest Pair Distance
class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()
        right = nums[-1] - nums[0]
        left = 0
        
        while left < right:
            mid = (left + right) // 2
            
            if (self.issmallpairs(nums, k, mid)):
                right = mid
            else:
                left = mid + 1
                
        return left
    
    # returns true if there are at least k pairs with distance <= mid
    def issmallpairs(self, nums: list[int], k:  int, mid: float) -> bool:
        count, left = 0, 0
        for right in range(1, len(nums)):
            while (nums[right] - nums[left] > mid):
                left += 1
            count += right - left
        
        return (count >= k)
    
soln = Solution()
    
print(soln.smallestDistancePair([1,3,1], 1))

print(Solution().smallestDistancePair([1,6,1], 3))