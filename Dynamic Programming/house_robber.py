# top-down approach with memoization using recursion
def house_robber(houses, current_index, memo):
    if current_index >= len(houses):
        return 0
    else:
        if current_index not in memo:
            steal_current = houses[current_index] + house_robber(houses, current_index + 2, memo)
            skip_current = house_robber(houses, current_index + 1, memo)
            memo[current_index] = max(steal_current, skip_current)
        return memo[current_index]
    
# bottom-up approach with tabulation/iterative computation
def house_robber2(houses):
    # Handle edge cases
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    if len(houses) == 2:
        return max(houses[0], houses[1])
    
    # Initialize dp array
    dp = [0] * len(houses)
    
    # Base cases
    dp[0] = houses[0]  # max money if we only have first house
    dp[1] = max(houses[0], houses[1])  # max money if we only have first two houses
    
    # Fill dp table
    for i in range(2, len(houses)):
        # At each house, we have two options:
        # 1. Rob current house + money from i-2 houses
        # 2. Skip current house and keep money from i-1 houses
        dp[i] = max(houses[i] + dp[i-2], dp[i-1])
    
    return dp[-1]
    

if __name__ == "__main__":
    houses = [6, 7, 1, 30, 8, 2, 4]
    print(house_robber2(houses, 0)) # 41

