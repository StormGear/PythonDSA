
# Template #1 for binary search
def binarySearch(nums: list[int], target: int):
    """
    The binarySearch function takes a sorted list of integers and a target integer as input, and returns
    the index of the target integer in the list if it exists, otherwise it returns -1.
    
    :param nums: The `nums` parameter is a list of integers that represents the sorted array in which we
    want to search for the target value
    :type nums: list[int]
    :param target: The target parameter is the value that we are searching for in the list
    :type target: int
    :return: The binarySearch function returns the index of the target element in the given list of
    numbers. If the target element is not found in the list, it returns -1.
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1

# Template #2
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if nums[left] == target:
        return left
    return -1


# Template #3 
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1
