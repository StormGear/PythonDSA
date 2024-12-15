
# Daily Coding Problem: Problem #82 [Easy]
# This problem was asked Microsoft.
class Solution:
    def __init__(self):
        self.buffer = []
        self.buffer_pointer = 0

    def read7(self):
        # This is a mock implementation of read7()
        # In a real scenario, this would be provided or implemented differently
        data = ["Hello w", "orld", ""]
        if hasattr(self, 'call_count'):
            self.call_count += 1
        else:
            self.call_count = 0
        return data[min(self.call_count, len(data) - 1)]

    def readN(self, n):
        result = []
        
        # First, use any leftover characters in the buffer
        while self.buffer_pointer < len(self.buffer) and n > 0:
            result.append(self.buffer[self.buffer_pointer])
            self.buffer_pointer += 1
            n -= 1
        
        # If we still need more characters
        while n > 0:
            chunk = self.read7()
            if not chunk:
                break  # End of file reached
            
            # Add necessary characters to result
            result.extend(chunk[:n])
            n -= len(chunk[:n])
            
            # Store any extra characters in buffer
            if len(chunk) > n:
                self.buffer = list(chunk[n:])
                self.buffer_pointer = 0
        
        return ''.join(result)

# Test the implementation
solution = Solution()
print(solution.readN(7))   # Output: Hello w
print(solution.readN(7))   # Output: orld
print(solution.readN(7))   # Output: 
print(solution.readN(100)) # Output: