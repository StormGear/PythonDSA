# sliding window

def best_total_price(prices, window_size):
    if len(prices) < window_size:
        return 0
    
    total = sum(prices[:window_size])
    maxtotal = total
    for i in range(len(prices)-window_size):
        total -= prices[i]
        total += prices[i+window_size]
        maxtotal = max(maxtotal, total)

    return total
