class Solution:
    # Time Complexity: O(n) where n is the number of elements in the list
    # Space Complexity: O(1)
    # Dynamic Programming approach
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
    
    # Two pointers approach
    # Time Complexity: O(n) where n is the number of elements in the list
    # Space Complexity: O(1)
    def maxProfit2(self, prices: list[int]) -> int:
        maxP = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                P = prices[r] - prices[l]
                maxP = max(maxP, P)
            else:
                l = r
            r += 1

        return maxP
    
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    print(s.maxProfit(prices))

# Think of it this way
