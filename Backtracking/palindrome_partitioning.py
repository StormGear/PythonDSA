class Solution:
    """
    Problem: [link](https://neetcode.io/problems/palindrome-partitioning)
    """
    def partition(self, s: str) -> list[list[str]]:
        """
        Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

        A palindrome string is a string that reads the same backward as forward.

        :param s: A string
        :return: A list of lists of strings
        """
        def is_palindrome(s):
            """
            `is_palindrome` returns `True` if the input string is a palindrome.

            :param s: A string
            :return: A boolean value
            """
            return s == s[::-1]

        def backtrack(start, path):
            """
            `backtrack` recursively explores a tree structure and returns all possible palindrome partitioning of `s`.

            :param start: The starting index of the current substring
            :param path: A list of strings
            :return: None
            """
            if start == len(s):
                res.append(path)
                return

            for i in range(start, len(s)):
                if is_palindrome(s[start:i+1]):
                    backtrack(i+1, path + [s[start:i+1]])

        res = []
        backtrack(0, [])
        return res
    
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)
if __name__ == "__main__":
    s = "aab"
    print(Solution().partition(s))