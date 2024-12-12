# Reverse Polish Notation
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def rpn(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens: 
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                num2, num1 = stack.pop(), stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append(int(token))
                    
        return stack.pop()
    
if __name__ == '__main__':
    soln = Solution()
    print(soln.rpn(["2", "1", "+", "3", "*"]))  # 9
    print(soln.rpn(["4", "13", "5", "/", "+"]))  # 6
    print(soln.rpn(["10", "6", "9", "3", "/", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22