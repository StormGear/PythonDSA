from collections import deque
from queue import LifoQueue 

stack = deque()

# push elements
stack.append(10)
stack.append(20)
stack.append(30)
 
# pop elements
stack.pop()

# check if empty
print(not stack)

stack2 = LifoQueue(3)

# push to the stack
stack2.put(10)
stack2.put(20)
stack2.put(30)
stack2.put(40, block=False )

# pop from the stack
print(stack2.get()) 

