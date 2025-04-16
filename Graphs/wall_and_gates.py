from collections import deque
from typing import List
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def add_room(r,c):
            if (r not in range(rows)) or (c not in range(cols)) or ((r,c) in visited) or (grid[r][c] == -1):
                return
            q.append([r,c])
            visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    nr, nc = r+dr, c + dc
                    add_room(nr,nc)
            dist += 1

        print(grid)

if __name__=='__main__':
    soln = Solution()
    grid = [
       [2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]
    ]
    soln.islandsAndTreasure(grid)
