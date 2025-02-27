
def find_mincost(cost, m, n):
    if m < 0 or n < 0:
        return float('inf')
    elif m == 0 and n == 0:
        return cost[m][n]
    else:
        option1 = find_mincost(cost, m-1, n)
        option2 = find_mincost(cost, m, n-1)
        option3 = find_mincost(cost, m-1, n-1)
        return cost[m][n] + min(option1, option2, option3)
    

if __name__=='__main__':
    cost = [[4, 7, 8,6,4],
            [6, 7, 3, 9, 2],
            [3, 8, 1, 2, 4],
            [7, 1, 7, 3, 7],
            [2, 9, 8, 9, 3]]
    print(find_mincost(cost, 4, 4))