# sum all the elements in a list
def sum(arr):
    # base case
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left_val = sum(left)
    right_val = sum(right)
    return left_val + right_val


if __name__== "__main__":
    arr = [2,3,5]
    print(sum(arr))