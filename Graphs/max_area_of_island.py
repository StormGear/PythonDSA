# Time Complexity: O(n*m) where n is the number of rows and m is the number of columns
# Space Complexity: O(n*m) for the visited set
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if (r not in range(rows)) or (c not in range(cols)) or (grid[r][c] == 0) or ((r,c) in visited):
                return 0
            
            visited.add((r,c))
            curr_area = 1
            directions = [[1,0], [-1,0], [0,1], [0, -1]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                curr_area += dfs(nr,nc)
            
            return curr_area

        area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, dfs(r,c))

        return area
    

if __name__=='__main__':
    soln = Solution()
    grid = [
        [0,1,1,0,1],
        [1,0,1,0,1],
        [0,1,1,0,1],
        [0,1,0,0,1]
        ]
    farm = [
        [0,1,1,0,1],
        [1,1,0,1,0],
        [0,1,1,1,0],
        [1,1,1,1,0],
        [1,1,1,1,1],
        [0,0,0,0,0]
    ]
    print(soln.maxAreaOfIsland(farm))
    print(soln.maxAreaOfIsland(grid))
    

        