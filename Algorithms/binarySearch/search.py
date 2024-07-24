# LeetCode search in rotated sorted array problem: https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        The function performs a binary search to locate the pivot (the smallest element) in a rotated
        sorted array.
        
        :param nums: A list of integers that may or may not be rotated
        :type nums: List[int]
        :param target: The target is the element that we are searching for in the given list of numbers
        :type target: int
        :return: the index of the target element in the given list of numbers. If the target element is
        not found, it returns -1.
        """
        size = len(nums)
        if size == 0:
            return -1
        
        # binary search to locate the pivot(the smallest element) in a rotated sorted array.
        # the pivot value is stored in the variable `left`
        left, right = 0, size-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

    # Binary search across an inclusive range [left_bound ~ right_bound]
        def binarySearch(left_bound, right_bound, target):
            """
            The binarySearch function performs a binary search on a sorted list of numbers to find the index
            of a target number, returning -1 if the target is not found.
            
            :param left_bound: The left_bound parameter represents the leftmost index of the array or list
            where the binary search will start
            :param right_bound: The right_bound parameter represents the index of the rightmost element in the
            array or list being searched
            :param target: The target parameter represents the value that we are searching for in the binary
            search algorithm
            :return: the index of the target element if it is found in the given range of the array
            (left_bound to right_bound). If the target element is not found, it returns -1.
            """
            left, right = left_bound, right_bound
            while left<= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1 

    
        # Binary search across the elements on the left of pivot
        if (answer := binarySearch(0, left - 1, target)) != -1:
            return answer

        # Binary search across the elements on the right of pivot
        return binarySearch(left, size-1, target)