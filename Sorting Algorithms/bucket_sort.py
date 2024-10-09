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
     

    
arr = [0.43, 0.33, 0.23 ,0.52, 0.25, 0.47, 0.51]
bucket_sort(arr)
print(arr)