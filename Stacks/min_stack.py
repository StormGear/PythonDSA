class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    # Time complexity: O(1)
    # Space complexity: O(n)
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)
        

        

    def pop(self) -> None:
        del self.stack[-1]
        del self.min_stack[-1]
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
    
if __name__ == '__main__':
    obj = MinStack()
    obj.push(5)
    obj.push(6)
    obj.push(4)
    obj.push(2)
    obj.push(1)
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
    obj.pop()
    print(obj.top())
        