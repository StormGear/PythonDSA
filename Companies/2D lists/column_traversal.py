# This problem was asked by Google.
# Daily Coding Problem: Problem #76 [Medium]
# time: O(n * m)
# space: O(1)
def column_traversal(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    nrows = len(matrix)
    ncols = len(matrix[0])
    cols_to_remove = 0
    for c in range(ncols):
        for r in range(1, nrows):
            if matrix[r][c] < matrix[r - 1][c]:
                cols_to_remove += 1
                print(matrix[r][c])
                break 

            
    return cols_to_remove

matrix1 = [
    ["c", "b", "a"],
    ["d", "a", "f"],
    ["g", "h", "i"]
]
matrix2 = [
    [["a", "b", "c", "d", "e", "f"]]
]
"""
zyx
wvu
tsr 
"""
matrix3 = [
    ["z", "y", "x"],
    ["w", "v", "u"],
    ["t", "s", "r"]
]

print(f'Minimum number of columns removed {column_traversal(matrix1)}')
print(f'Minimum number of columns removed {column_traversal(matrix2)}')
print(f'Minimum number of columns removed {column_traversal(matrix3)}')