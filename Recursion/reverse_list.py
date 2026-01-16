# reverse a list
def reverse(arr):
    # base case
    if len(arr) < 2:
        return arr

    # recursive case
    left = [arr[0]] # [2]
    right = arr[1:] #[ 3,5]

    left_val = reverse(left) # [2]
    right_val = reverse(right) # [3,5]
    return right_val + left_val 

if __name__=="__main__":
    arr = [2,3,5]
    print(reverse(arr))