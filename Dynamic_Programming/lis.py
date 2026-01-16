# longest increasing subsequence - This question was asked by Microsoft
# time: O(n^2) space: O(1)
def lengthOfLIS(nums):
    if not nums:
        return 0

    # Initialize dp array where dp[i] represents the length of LIS ending at index i
    dp = [1] * len(nums) # Define state/dp array or table

    # Variable to store the maximum length of the LIS found
    maxLength = 1 # Initialize the base case

    # Loop through the array to build the dp array 
    # iterative approach
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        # Update the maximum length found so far
        maxLength = max(maxLength, dp[i])


    return maxLength


# time: O(n log n) space: O(1)
def lengthOfLIS_optimized(nums):
    if not nums:
        return 0

    temp = [nums[0]] # temp array to store the smallest tail of all increasing subsequences with different lengths

    for i in range(1, len(nums)):
        if nums[i] > temp[-1]:
            temp.append(nums[i])
        else:
            # Find the index of the smallest number >= nums[i]
            left, right = 0, len(temp) - 1
            while left < right:
                mid = (left + right) // 2
                if temp[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            temp[left] = nums[i] # Replace it with nums[i]

    return len(temp)

def lengthOfLIS_bisectleft(nums):
    from bisect import bisect_left
    sub = []  # will store the potential tails of subsequences
    for x in nums:
        # Find insertion point for x in sub
        i = bisect_left(sub, x)
        if i == len(sub):
            sub.append(x)   # extend the LIS
        else:
            sub[i] = x      # replace to maintain minimal tail
    return len(sub)