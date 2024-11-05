class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        # use memoization
        # time complexity: O(n)
        # space complexity: O(n)
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
            return memo[n]

    def climbStairs2(self, n: int) -> int:
        # use tabulation
        # time complexity: O(n)
        # space complexity: O(n)
        arr = [1, 2] + [1] * (n-2) 
        if n == 1:
            return arr[0]
        if n == 2:
            return arr[1]
        else:
            for i in range(2, n): # 4. Iterative Computation
                arr[i] = arr[i-1] + arr[i-2] # 2. Recurrence Relation
            
        return arr[n-1] # 5. Extract Solution
    
if __name__ == "__main__":
    n = 10  # Change this value to compute a different Fibonacci number
    memo = {1:1, 2:2}
    soln = Solution()
    print(f"Memoization dictionary after calculating climbStairs({n}): {soln.climbStairs(n, memo)}")
    # print(f"Tabulation array after calculating climbStairs({i}): {Solution().climbStairs2(i)}")