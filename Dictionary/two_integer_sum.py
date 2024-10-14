class Solution:
    # Time: O(n) Space: O(n)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
         The two sum problem
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

# nums = [3,4,5,6], target = 7

# Output: [0,1]