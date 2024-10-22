# Solving the longest common subsequence problem using recursion
count = 0
def lcs(a: str, b:str) -> int:
    ptr_a: int = 0
    ptr_b: int = 0
    global count
    count += 1

    # End of the string
    if ptr_a == len(a) or ptr_b == len(b):
        return 0
    
    # If the characters are the same, a match is found
    elif a[ptr_a] == b[ptr_b]:
        return 1 + lcs(a[ptr_a+1:], b[ptr_b+1:])
    
    # If the characters are different, move the pointer of the string with the larger length
    else:
        return max(lcs(a[ptr_a+1:], b), lcs(a, b[ptr_b+1:]))
    
# a = "bd"
# b = "abcd"
# lcs(a, b)

# Implement the function lcs using dynamic programming
def lcs2(a: str, b:str) -> int:
    n = len(a)
    m = len(b)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n][m]

   
    
if __name__ == '__main__':
    a = "bd"
    b = "abcd"
    print(f"Length of LCS is {lcs2(a, b)}")  # Output: 2
    # print(f"Number of recursive calls: {counter}")  # Output: 9
   