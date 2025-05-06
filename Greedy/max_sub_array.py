from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        curr_sum = 0

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            max_sub = max(max_sub, curr_sum)
        return max_sub