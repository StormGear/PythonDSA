

# Generate a set of valid parenthesis 
# 
class Solution:
    """
    Problem: [link](https://neetcode.io/problems/generate-parentheses)
    """
    def generateParentheses(self, n: int) -> int:
        stack = []
        res = []


        def backtrack(opened_count, closed_count):
            if opened_count == closed_count == n:
                res.append("".join(stack))
                return

            # Add open parentheses if open count < n
            if opened_count < n:
                stack.append("(")
                backtrack(opened_count + 1, closed_count)
                stack.pop()

            # Add close parentheses if closed count < open count
            if closed_count < opened_count:
                stack.append(")")
                backtrack(opened_count, closed_count + 1)
                stack.pop()

        backtrack(0, 0)
        return res
    

# Time complexity: O(4^n/sqrt(n))
# Space complexity: O(n)
if __name__ == '__main__':
    soln = Solution()
    print(soln.generateParentheses(3))  # ['((()))', '(()())', '(())()', '()(())', '()()()']
    print(soln.generateParentheses(2))
