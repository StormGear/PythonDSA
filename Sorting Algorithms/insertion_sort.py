# time: O(n^2) space: O(1)
# Take first element and compare it with the elements to its left in the sorted array. If the element to its left is greater than the current element, swap them. Continue this process until the element is in its correct position.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]: # Current element is less than the element to its left
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr

print(insertion_sort([4,6,8,3,2,5,7,8,9, 1]))