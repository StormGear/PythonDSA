
# House Robber, rob houses on a line, but avoid robbing adjacent houses
count1 = 0
def house_robber(houses: list[int], currentHouse: int) -> int:
    if currentHouse > len(houses) - 1:
        return 0
    global count1
    count1 += 1
    stealH1 = houses[currentHouse] + house_robber(houses, currentHouse + 2)
    skipH1 = house_robber(houses, currentHouse + 1)
    return max(stealH1, skipH1)

# House Robber, rob houses on a line, but avoid robbing adjacent houses
count2 = 0
def house_robber_memo(houses: list[int], currentHouse: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    if currentHouse in memo:
        return memo[currentHouse]
    if currentHouse > len(houses) - 1:
        return 0
    global count2
    count2 += 1
    stealH1 = houses[currentHouse] + house_robber_memo(houses, currentHouse + 2, memo)
    skipH1 = house_robber_memo(houses, currentHouse + 1, memo)
    memo[currentHouse] = max(stealH1, skipH1)
    return memo[currentHouse]

def house_robber_tab(houses: list[int]) -> int:
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    
    # dp table to store maximum money that can be robbed up to index i
    dp = [0] * len(houses)
    
    # Base cases
    dp[0] = houses[0]  # only first house
    dp[1] = max(houses[0], houses[1])  # max of first two houses
    
    # Fill the dp table
    for i in range(2, len(houses)):
        dp[i] = max(dp[i-1],  # skip current house
                   dp[i-2] + houses[i])  # rob current house + money from i-2 houses
    
    return dp[-1]



houses = [6,7,1,30,8,2,4]
# houses = [20, 50]
print(house_robber_tab(houses))
print(count2) 
