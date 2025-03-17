class Solution:
    def subsetsWithDup(self, nums: list[int])-> list[list[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return
            
            # all subsets including nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            # exclude nums[i]
            subset.pop()

            # skip duplicates
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            # all subsets excluding nums[i]
            backtrack(i+1, subset)

        backtrack(0, [])
        return res
