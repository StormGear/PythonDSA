class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def valid_paretheses(self, s):
        charMap = {')' : '(', ']' : '[', '}' : '{'}
        stack = [] # for storing open parentheses only

        for char in s:
            if char in charMap.values():
                stack.append(char)
            else:
                if len(stack) == 0 or charMap[char] != stack.pop():
                    return False
                
        # at the end all open parenthesis should have a match   
        return len(stack) == 0
    
if __name__ == '__main__':
    soln = Solution()
    print(soln.valid_paretheses('[{()}]'))
    print(soln.valid_paretheses('[]'))
    print(soln.valid_paretheses('[(])'))
    print(soln.valid_paretheses(')'))
    print(soln.valid_paretheses('('))
