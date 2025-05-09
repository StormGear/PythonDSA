class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for c in range(len(text1)+1)] for r in range(len(text2)+1)]

        for r in range(len(text2)-1, -1, -1):
            for c in range(len(text1)-1, -1, -1):
                if text1[c] == text2[r]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r][c+1], dp[r+1][c])

        return dp[0][0]
    