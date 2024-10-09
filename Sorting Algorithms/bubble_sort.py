# time:  O(n^2)            space: O(1)
def bubble_sort(arr):
    size = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, size):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

print(bubble_sort([4,6,8,3,2,5,7,8,9]))