# Fibonacci sequence with a recursive approach
def fibonacci1(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)

# Fibonacci sequence with an iterative approach or tabulation
def fibonacci2(n):
    arr = [0, 1]
    if n <= 0:
        return arr[0]
    if n == 1:
        return arr[1]
    else:
        for i in range(2, n+1):
            arr.append(0)
            arr[i] = arr[i-1] + arr[i-2]
            
    return arr[n]

# fibonacci sequence with memoization
def fibonacci3(n):
    memo = {0:0, 1:1}
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci3(n-1) + fibonacci3(n-2)
        return memo[n]



# Example usage:
if __name__ == "__main__":
    n = 5  # Change this value to compute a different Fibonacci number
    print(f"Fibonacci number at position {n} is {fibonacci3(n)}")