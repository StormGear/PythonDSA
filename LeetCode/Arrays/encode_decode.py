class Solution:
    # Time Complexity: O(n) where n is the number of strings
    # Space Complexity: O(1) 
    def encode(self, strs: list[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + ":" + s

        return res

    # Time Complexity: O(n) where n is the number of strings
    # Space Complexity: O(1)
    def decode(self, s: str) -> list[str]:
        res, i = [], 0

        while i < len(s):
            # j tracks the position of the delimiter
            j = i
            while s[j] != ":":
                j += 1

            length = int(s[i:j]) # the length of the string
            res.append(s[j+1:j+1+length])

            i = j+1+length

        return res


    
if __name__ == "__main__":
    strs = ["Hello", "World", "Python", "Programming"]
    s = Solution()
    encoded = s.encode(strs)
    print(f'Encoded string: {encoded}')
    decoded = s.decode(encoded)
    print(f'Decoded string: {decoded}')