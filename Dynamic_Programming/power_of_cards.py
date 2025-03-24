# Got this question from TestGorilla
# You can a list of cards with powers indicated by integer values. The objective to find the maximum amount of cards to pick
# such that your power remains at least 0
# if it's a positive card your power increases, it is negative your power decreases
# Eg: cards =  [5,2,-3,-1,5] n = 5 (total number of cards)
# Output: 4
# Explanation: Pick 5, 2, -3, 5

def max_cards(cards):
    n = len(cards)
    def maximize_power(index, power):
        if index == n:
            return 0
        elif power + cards[index] >= 0:
            return 1 + maximize_power(index+1, power + cards[index])
        else:
            return max(maximize_power(index+1, power), maximize_power(index+1, power + cards[index]))
    return maximize_power(0, 0)

def max_cards_dp(cards):
    if not cards:
        return 0
    if len(cards) == 1 and cards[0] >= 0:
        return 1 # return 1 actually since you pick just 1 card
    
    dp = [0] * len(cards) 
    power = 0

    # set base cases, select the first card if it's positive
    # and select the first two cards if the sum of the first two cards is positive
    if cards[0] >= 0:
        dp[0] = 1
        power += cards[0]
    if power + cards[1] >= 0:
        dp[1] += dp[0] + 1
        power += cards[1]

    for i in range(2, len(cards)):
        # At each card, we have two options:
        # 1. Pick the current card and add the power from i-th card
        # 2. Skip the current card and keep the power from i-1 cards
        if power + cards[i] >= 0:
            power += cards[i]
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]

    return dp[-1]

print(max_cards_dp([5,2,-3,-1,5]))

