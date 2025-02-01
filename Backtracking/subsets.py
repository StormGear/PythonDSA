class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # include this value in the path
            subset.append(nums[i])
            dfs(i+1) # move to the next

            # exclude this value in the path
            subset.pop()
            dfs(i+1) 

        dfs(0)
        return res
    

if __name__ == '__main__':
    soln = Solution()
    soln.subsets([1,2,3])