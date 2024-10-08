# Daily Coding Problem: Problem #74 [Medium] - This question was asked by Apple
# time: O(n * m)
# space: O(1)
def row_traversal(matrix, x):
    nrows = len(matrix)
    ncols = len(matrix[0])
    count = 0
    for r in range(nrows):
        for c in range(ncols):
            if matrix[r][c] == x:
                count += 1
    return count
"""
| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 
"""
matrix1 = [
    [1, 2, 3, 4, 5, 6],
    [2, 4, 6, 8, 10, 12],
    [3, 6, 9, 12, 15, 18],
    [4, 8, 12, 16, 20, 24],
    [5, 10, 15, 20, 25, 30],
    [6, 12, 18, 24, 30, 36]
]

x = 12
print(f'The number of occurences of the number "{x}" in the matrix1 is: {row_traversal(matrix1, x)}')