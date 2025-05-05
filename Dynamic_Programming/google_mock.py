# Problem from the google  mock interview video on youtube

def largest_square(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_square_length = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_square_length = max(max_square_length, dp[i][j])

    return max_square_length ** 2


if __name__ == "__main__":
    farm = [
        [0,1,1,0,1],
        [1,1,0,1,0],
        [0,1,1,1,0],
        [1,1,1,1,0],
        [1,1,1,1,1],
        [0,0,0,0,0]
    ]
    print(largest_square(farm))
    # Output: 9