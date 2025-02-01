

# Include a number on one branch and exclude it on another branch
class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(nums) or total > target:
                return

            # include nums[i]
            curr.append(nums[i])
            dfs(i, curr, total+nums[i])

            # exclude nums[i]
            curr.pop()
            dfs(i+1, curr, total)

        dfs(0, [], 0)
        return res