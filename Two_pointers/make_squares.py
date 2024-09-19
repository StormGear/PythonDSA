class Solution:
    # O(nlogn) due to the sorting algorithm for `sorted`
    def makeSquares(self, arr):
        squares = [] 
        # TODO: Write your code here
        for i in arr:
            squares.append(i*i)
            squares = sorted(squares)
        return squares

    # Time: O(n)
    # Space: O(n)
    def makeSquares2(self, arr):
        # Get the length of the input array
        n = len(arr)
    
        # Create a list to store the squares, initialized with zeros
        squares = [0] * n
        
        # Initialize the index for the highest square in the output array
        highestSquareIdx = n - 1
        
        # Initialize two pointers for the left and right ends of the input array
        left, right = 0, n - 1
        
        # Iterate over the input array from both ends towards the center
        while left <= right:
            # Calculate the squares of the elements at the left and right pointers
            leftSquare = arr[left] * arr[left]
            rightSquare = arr[right] * arr[right]
    
            # Compare the squares and store the larger square in the output array
            if leftSquare > rightSquare:
                squares[highestSquareIdx] = leftSquare
                left += 1
            else:
                squares[highestSquareIdx] = rightSquare
                right -= 1
        
            # Move to the next index in the output array
            highestSquareIdx -= 1

        # Return the resulting list of squares
        return squares

print(Solution().makeSquares2([-2, -1, 0, 2, 3]))