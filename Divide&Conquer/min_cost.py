

# Find the minimum cost to reach from the top-left cell to the bottom-right cell of a matrix
# The cost of a cell is the number written in that cell
# You can only move right or down from a cell
# You have to start from the top-left cell and reach the bottom-right cell
# You have to find the path that has the minimum cost
# The cost of a path is the sum of the costs of the cells in that path  

# Start from the upper indexes and move towards the lower indexes
# At each cell, you have two options: move left or move up
# Find the minimum cost of the two options
# Add the cost of the current cell to the minimum cost of the two options
def find_mincost(cost, m, n):
    if m < 0 or n < 0:
        return float('inf')
    elif m == 0 and n == 0:
        return cost[m][n]
    else:
        option1 = find_mincost(cost, m-1, n)
        option2 = find_mincost(cost, m, n-1)
        return cost[m][n] + min(option1, option2)
    

if __name__=='__main__':
    cost = [[4, 7, 8,6,4],
            [6, 7, 3, 9, 2],
            [3, 8, 1, 2, 4],
            [7, 1, 7, 3, 7],
            [2, 9, 8, 9, 3]]
    print(find_mincost(cost, 4, 4))