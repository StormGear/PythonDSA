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
        print(f'dp so far: {dp}')
        maxLength = max(maxLength, dp[i])


    return maxLength