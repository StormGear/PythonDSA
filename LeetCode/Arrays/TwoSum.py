# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution(object):
    def twoSum_brute(self, nums: list[int], target: int) -> list[int]:
        """
        The function "twoSum" takes in a list of integers "nums" and a target integer "target", and
        returns a list of two indices from "nums" whose corresponding values add up to the target.
        
        :param nums: A list of integers
        :type nums: list[int]
        :param target: The target is the sum that we are trying to find using two numbers from the given
        list
        :type target: int
        """
        n = len(nums)
        for left in range(n):
            for right in range(left + 1, n):
                if nums[left] + nums[right] == target:
                    return [left, right]
                
        # If no two numbers add up to the target, return an empty list
        return []
    
    def twoSum_hashmap(self, nums: list[int], target: int) -> list[int]:
        visited = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            
            if remaining in visited:
                return [i, visited[remaining]]
            
            visited[value] = i 
        return []
            
            