
# Find the duplicate number - Floyd's Algorithm for cycle detection, A linked list cycle problem

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # initialize tortoise and hare to the first element in the array
        tortoise = nums[0]
        hare = nums[0]
        
        # Phase 1: Detect the intersection point
        while True:
            # tortoise moves one step, hare moves two steps
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            # check if they meet at an intersection point
            if tortoise == hare:
                break
                
        # Phase 2: Find the entrance to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            # Both move one step at a time until they meet
            tortoise = nums[tortoise]
            hare = nums[hare]
            
        # The meeting point is the duplicate number
        return hare