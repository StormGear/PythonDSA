# Implement the function lcs using dynamic programming (2D - DP)
# time complexity: O(n*m)
# space complexity: O(n*m)
subsequence = ""
def lcs2(a: str, b:str) -> int:
    m = len(a)
    n = len(b)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    global subsequence 
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                subsequence = subsequence + a[i-1] 
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

   
    
if __name__ == '__main__':
    a = "bd"
    b = "abcd"
    print(f"Length of LCS is {lcs2(a, b)} with subsequence {subsequence}")  # Output: 2