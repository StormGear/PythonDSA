# time:  O(n^2)            space: O(1)
# Compare adjacent elements and swap them if they are in the wrong order.
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


def bubble_sort2(arr):
    size = len(arr)

    for i in range(size):
        for j in range(size-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(bubble_sort([4,6,8,3,2,5,7,8,9]))
print(bubble_sort2([4,6,8,3,2,5,7,8,9]))