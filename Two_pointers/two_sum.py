# solving the two sum problem using two pointers
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums) - 1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                return [left, right]
            
        return [-1, -1]
            