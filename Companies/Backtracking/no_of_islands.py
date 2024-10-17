
# This problem was asked by Amazon.
# Daily Coding Problem: Problem #84 [Medium]

class Solution:
    # Time complexity: O(n*m)
    # Space complexity: O(n*m)
    def num_islands(self, grid: list[list[str]])-> int:
        if not grid:
            return 0
        
        nrows, ncols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            queue = [(r, c)]
            visited.add((r, c))
            while queue:
                r, c = queue.pop(0)
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # down, up, right, left
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(nrows)) and (nc in range(ncols)) and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))



        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands


'''
1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
'''
grid = [
    ["1", "0", "0", "0", "0"],
    ["0", "0", "1", "1", "0"],
    ["0", "1", "1", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["1", "1", "0", "0", "1"],
    ["1", "1", "0", "0", "1"]
]
print('Number of islands:', Solution().num_islands(grid)) # 4
