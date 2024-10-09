# time: O(n^2) space: O(1)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr

print(insertion_sort([4,6,8,3,2,5,7,8,9]))