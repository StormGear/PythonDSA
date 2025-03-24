# Fibonacci sequence with a recursive approach
# When solving the Fibonacci sequence with a recursive approach, we can use memoization to store the results of the subproblems.
# In dynamic programming, memoization is an optimization technique used to store the results of expensive function calls and return the cached result when the same inputs occur again.
# Below is the outlined strategy.
def fibonacci1(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)

# Fibonacci sequence with an iterative approach or tabulation
def fibonacci2(n):
    arr = [0, 1] + [1] * (n-1) # 3. Initialization: Initialize the base case(s) of your DP array. ||  # 1. Define the State
    if n <= 0:
        return arr[0]
    if n == 1:
        return arr[1]
    else:
        for i in range(2, n+1): # 4. Iterative Computation
            arr[i] = arr[i-1] + arr[i-2] # 2. Recurrence Relation
            
    return arr[n] # 5. Extract Solution

# fibonacci sequence with memoization
def fibonacci3(n, memo={}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci3(n-1, memo) + fibonacci3(n-2, memo)
        return memo[n]



# Example usage:
if __name__ == "__main__":
    n = 10  # Change this value to compute a different Fibonacci number
    memo = {0: 0, 1: 1}
    print(f"Memoization dictionary after calculating Fibonacci({n}): {fibonacci3(n, memo)}")