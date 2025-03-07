from functools import lru_cache

# top-down approach with memoization using recursion
def number_factor(n: int, memo={0:1,1:1,2:1,3:2}) -> int:
    # use memoization
    # time complexity: O(n)
    # space complexity: O(n)
    if n in memo:
        return memo[n]
    else:
        memo[n] = number_factor(n-1, memo) + number_factor(n-3, memo) + number_factor(n-4, memo)
        return memo[n]
    
def number_factor_top_down(n: int) -> int:
    if n < 0:
        return 0
    elif n in {0, 1, 2}:
        return 1
    elif n == 3:
        return 2
    
    return number_factor(n-1) + number_factor(n-3) + number_factor(n-4)

@lru_cache(maxsize=None)
def number_factor_cache(n: int) -> int:
    if n < 0:
        return 0
    elif n in {0, 1, 2}: return 1
    elif n == 3: return 2
    return number_factor(n-1) + number_factor(n-3) + number_factor(n-4)

def number_factor_cache_stats():
    print(number_factor_cache.cache_info())

# bottom-up approach with tabulation/iterative computation
def number_factor_bottom_up(n: int) -> int:
    if n < 0:
        return 0
    dp = [1,1,1,2]
    
    for i in range(4, n + 1):
        dp.append(dp[i-1] + dp[i-3] + dp[i-4])
    
    return dp[n]


if __name__ == "__main__":
    print(number_factor(5)) # 6
    print(number_factor(10)) # 64
    print(number_factor_bottom_up(5)) # 6
    print(number_factor_cache(10)) # 64
    number_factor_cache_stats()