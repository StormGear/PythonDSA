class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # assuming both nums1 and nums2 cannot be empty
        nums1_size = len(nums1)
        nums2_size = len(nums2)
        if (nums1_size > nums2_size):
            return self.findMedianSortedArrays(nums2, nums1) # swapping to make nums1 smaller
        
        start = 0
        end = nums1_size
        realmidinmergedarray = (nums1_size + nums2_size + 1) // 2
        
        while (start <= end):
            mid = (start + end) // 2
            leftnums1_size = mid
            leftnums2_size = realmidinmergedarray - mid
            
            # checking overflow of indices
            leftnums1 = nums1[leftnums1_size - 1] if (leftnums1_size > 0) else float('-inf')
            leftnums2 = nums2[leftnums2_size - 1] if (leftnums2_size > 0) else float('-inf')
            rightnums1 = nums1[leftnums1_size] if (leftnums1_size <  nums1_size) else float('inf')
            rightnums2 = nums2[leftnums2_size] if (leftnums2_size < nums2_size) else float('inf')
            
            # if correct partition is done
            if leftnums1 <= rightnums2 and leftnums2 <= rightnums1:
                # if total length is odd
                if (nums1_size + nums2_size) % 2 == 1:
                    return max(leftnums1, leftnums2)
                # if total length is even
                else:
                    return (max(leftnums1, leftnums2) + min(rightnums1, rightnums2)) / 2    
            # if partition is not correct
            elif leftnums1 > rightnums2:
                end = mid - 1
            else:
                start = mid + 1
            