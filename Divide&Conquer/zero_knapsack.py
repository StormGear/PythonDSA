
# Zero knapsack problem: Given weights and profits of n items, put these items in a knapsack of capacity W to get the maximum total profit in the knapsack.
class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit

def zero_knapsack(items: list[Item], capacity: int, current_index: int):
    if capacity <= 0 or current_index < 0 or current_index >= len(items):
        return 0
    elif items[current_index].weight <= capacity:
        include_current = items[current_index].profit + zero_knapsack(items, capacity-items[current_index].weight, current_index+1)
        exclude_current = zero_knapsack(items, capacity, current_index+1)
        return max(include_current, exclude_current)
    else:
        return 0
    

if __name__ == "__main__":
    items = [Item(1, 6), Item(2, 10), Item(3, 12)]
    print(zero_knapsack(items, 5, 0)) # 22
   