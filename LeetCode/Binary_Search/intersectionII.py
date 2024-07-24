from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Create Counters for both arrays
        count1 = Counter(nums1)
        count2 = Counter(nums2)
       
        
        # Find the intersection of the two Counters
        intersection = count1 & count2
      
        # Flatten the intersection Counter into a list
        result = []
        for num, freq in intersection.items():
            result.extend([num] * freq)

        return result
    
    
# Example 1
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(Solution().intersect(nums1, nums2))  # Output: [2, 2]
