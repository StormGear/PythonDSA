

# Include a number on one branch and exclude it on another branch
# Combination Sum

class Solution:
    """
    Problem: [link](https://neetcode.io/problems/combination-target-sum)
    """
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i : int, curr: list[int], total: int) -> None:
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return

            # include nums[i]
            curr.append(nums[i])
            dfs(i, curr, total+nums[i]) # reuse the same element
            # exclude nums[i]
            curr.pop()

            # move to the next element
            dfs(i+1, curr, total)

        dfs(0, [], 0)
        return res
    
if __name__ == '__main__':
    nums = [2,3,6,7]
    target = 7
    print(Solution().combinationSum(nums, target)) # [[2,2,3],[7]]