# Reverse Polish Notation
class Solution:
    def rnp(self, tokens: list[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
                    
        return stack.pop()
    
if __name__ == '__main__':
    soln = Solution()
    print(soln.rnp(["2", "1", "+", "3", "*"]))  # 9
    print(soln.rnp(["4", "13", "5", "/", "+"]))  # 6
    print(soln.rnp(["10", "6", "9", "3", "/", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22