class Solution:
    memo = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        # use memoization
        # time complexity: O(n)
        # space complexity: O(n)


        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.memo[n]

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
    n = 10  # Change this value to compute a different Fibonacci numberd
    for i in range(1, n+1):
        print(f"Memoization dictionary after calculating climbStairs({i}): {Solution().climbStairs(i)}")
        print(f"Tabulation array after calculating climbStairs({i}): {Solution().climbStairs2(i)}")