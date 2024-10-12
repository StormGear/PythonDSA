# Daily Coding Problem: Problem #79 [Medium]
# This problem was asked by Facebook.
# time complexity: O(N) space complexity: O(1)
def can_be_non_decreasing(arr):
    count = 0  # To count the number of violations
    n = len(arr)
    
    # iterate through the array to the last but one element for violations
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            count += 1
            if count > 1:
                return False  # More than one violation

            # Check if we can modify arr[i] or arr[i + 1]
            if i == 0 or arr[i - 1] <= arr[i + 1]:
                arr[i] = arr[i + 1]  # Modify arr[i] to arr[i + 1]
            else:
                arr[i + 1] = arr[i]  # Modify arr[i + 1] to arr[i]
    
    return True

# Test cases
print(can_be_non_decreasing([10, 5, 7]))  # Output: True
print(can_be_non_decreasing([10, 5, 1]))  # Output: False
