
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        curr_min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[curr_min]:
                curr_min = j

        arr[i], arr[curr_min] = arr[curr_min], arr[i]

    return arr


arr = [2,6,5,1,3,4]
print(selection_sort(arr))