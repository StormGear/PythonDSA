# Problem - Search in a sorted Array of unknown size


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

# This is ArrayReader's API interface.
class ArrayReader:
    def __init__(self, array):
        self.array = array

    def get(self, index):
        """
        The function returns the element at the given index in the array, or positive infinity if the
        index is out of range.
        
        :param index: The index parameter represents the index of the element that you want to retrieve
        from the array
        :return: If the index is greater than or equal to the length of the array, the function returns
        positive infinity (float('inf')). Otherwise, it returns the element at the specified index in
        the array.
        """
        if index >= len(self.array):
            return float('inf')
        return self.array[index]

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = 0, 20000
        while left < right:
            print(f"left:{left}   and Right: {right}")
            mid = (left + right) >> 1
            print(f"mid: {mid}")
            if reader.get(mid) >= target:
                right = mid
            else:
                left = mid + 1
        return left if reader.get(left) == target else -1
       
  
  
# Test Cases
  
# Input: array = [-1,0,3,5,9,12], target = 9
# Output: 4
array1 = [-1, 0, 3, 5, 9, 12]
target1 = 9
reader = ArrayReader(array1)
print(Solution().search(reader, target1)) # result = 4

# Input: array = [-1,0,3,5,9,12], target = 2
# Output: -1(
# array2 = [-1, 0, 3, 5, 9, 12]
# target2 = 2
# reader2 = ArrayReader(array2)
# print(Solution().search(reader2,target2))