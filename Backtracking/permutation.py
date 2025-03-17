class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if not len(nums):
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res
    
# This code implements a recursive approach to generate all possible permutations of a given list of numbers. Here's how it works:

# 1. **Base Case**: 
#    - If the input list is empty, returns `[[]]` (a list containing an empty list)

# 2. **Recursive Step**:
#    - Takes first number (`nums[0]`) and gets all permutations of remaining numbers (`nums[1:]`)
#    - For each permutation in the recursive result:
#      - Inserts the first number at every possible position

# For example, with `nums = [1,2,3]`:
# - First gets permutations of `[2,3]`
# - Then inserts `1` at each possible position in each permutation of `[2,3]`

# Sample flow:
# ```
# [1,2,3] -> get perms of [2,3]
#   [2,3] -> get perms of [3]
#     [3] -> get perms of []
#       [] -> returns [[]]
#     Insert 3 -> [[3]]
#   Insert 2 -> [[2,3], [3,2]]
# Insert 1 -> [[1,2,3], [2,1,3], [2,3,1], ...]
# ```

# This is an elegant recursive solution, though it uses extra space for copying lists. Time complexity is O(n!), where n is the length of input array.