class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxCount = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            maxCount = max(maxCount, count[s[r]])

            while (r-l + 1) - maxCount > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)

        return res
    
if __name__ == "__main__":
    char1 = Solution()
    print(char1.character_replacement("ABAB", 2)) # 4
