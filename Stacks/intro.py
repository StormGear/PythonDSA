# Last In First Out(LIFO)

# Implementation of stack data structure using list

stack = []

# Perform push operation
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# Perform the pop operation
print(stack.pop()) 

# check if stack is empty
print(len(stack) == 0) 

# Access the last element or top of stack
stack[-1]