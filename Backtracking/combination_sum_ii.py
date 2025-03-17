# Combination Sum II

class Solution:
    def combination_sum_ii(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, total):
            """
            `dfs` recursively explores a tree structure and appends a copy of the current path
            to a result list when the target total is reached.
            
            :param i: The current index in the `candidates` list that is being considered in the depth-first
            :param curr: The current combination
            :param total: The sum of the current combination
            """
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i == len(candidates):
                return
            
            # include current element
            curr.append(candidates[i])
            # move to the next element
            dfs(i+1, curr, total+candidates[i])
            # exclude current element
            curr.pop()

            # skip duplicates
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            # move to the next element
            dfs(i+1, curr, total)


        dfs(0, [], 0)
        return res


if __name__=='__main__':
    candidates = [9,2,2,4,6,1,5]
    target = 8
    print(Solution().combination_sum_ii(candidates, target)) # [[1,2,5],[2,2,4],[2,6]]

            

