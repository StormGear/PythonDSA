class Solution:
    def letters(self, word:str) -> list[str]:
        n = len(word)
        res = []
        subset = []

        def backtrack(i):
            if i == n:
                res.append("".join(subset[:]))
                return
            
            # don't include word[i]
            backtrack(i + 1)

            # include word[i]
            subset.append(word[i])
            backtrack(i + 1)
            subset.pop()


        backtrack(0)
        return res
    
if __name__ == "__main__":
    word = "xyz"
    print(Solution().letters(word))