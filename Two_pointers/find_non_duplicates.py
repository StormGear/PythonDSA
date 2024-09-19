# solution to find non duplicate number instances
# Time: O(n)
# Space: O(1)
class Solution:
    def find_non_duplicates(self, arr: list[int]) -> int:
        """Return the number of first non-duplicate in the array."""
        current_index, next_non_duplicate = 1, 0
        
        while current_index < len(arr):
            if arr[next_non_duplicate - 1] != arr[current_index]:
                arr[next_non_duplicate] = arr[current_index]
                next_non_duplicate += 1
                
            current_index += 1
            
        return next_non_duplicate
        