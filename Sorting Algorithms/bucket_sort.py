from math import floor

def bucket_sort(arr):
    if not arr:
        return
    
    size = len(arr)
    buckets = [[] for i in range(size)] 

    # insert elements from the arr into the buckets 
    for i in range(0, size):
        bucket_idx = floor(arr[i] * size)
        buckets[bucket_idx].append(arr[i])

    print(f"After inserting: {buckets}")

    #sort the list in the buckets
    for i in range(0, size):
        buckets[i].sort()

    idx = 0
    for i in range(0, size):
        for j in range(0, len(buckets[i])):
            arr[idx] = buckets[i][j]
            idx += 1

import math
# Time Complexity: O(n) Space Complexity: O(n)
# Create a list of buckets, distribute the elements of the input array into the buckets with a given formula,
# sort elements in each bucket, and then merge the elements from the buckets back into the input array.
def bucket_sort2(arr):
    if not arr:
        return
    
    number_of_buckets = math.floor(math.sqrt(len(arr)))
    buckets = [[] for _ in range(number_of_buckets)] 

    # insert elements from the arr into the buckets 
    for i in arr:
        bucket_idx = math.ceil(i * number_of_buckets/ max(arr)) - 1  
        buckets[bucket_idx].append(i)

    print(f"After inserting: {buckets}")

    # sort the list in the buckets
    for i in range(len(buckets)):
        buckets[i].sort()

    # merge the elements from the buckets back into the input array
    idx = 0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            arr[idx] = buckets[i][j]
            idx += 1
     

     

arr = [0.43, 0.33, 0.23 ,0.52, 0.25, 0.47, 0.51]
arr2 = [0.43, 0.33, 0.23 ,0.52, 0.25, 0.47, 0.51]
bucket_sort(arr)
bucket_sort2(arr2)
print(arr)
print(arr2)