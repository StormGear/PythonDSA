
# Time Complexity: O(n^2) Space Complexity: O(1)
# Select the smallest element from the array and moving it to the front of the unsorted part of the array.
def selection_sort(arr):
    for i in range(len(arr)):
        curr_min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[curr_min]:
                curr_min = j

        arr[i], arr[curr_min] = arr[curr_min], arr[i]

    return arr

def selection_sort2(arr):
    pass



arr = [2,6,5,1,3,4]
print(selection_sort(arr))