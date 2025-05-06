from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque() # add all rotten fruits
        time, fresh = 0, 0 # time taken, number of fresh fruits

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                # count all fresh fruits 
                if grid[r][c] == 1:
                    fresh += 1
                # add all rotten fruits to the queue
                if grid[r][c] == 2:
                    rotten.append([r,c])

        directions = [[0,-1], [0,1], [1,0], [-1,0]]
        while rotten and fresh > 0:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    # if within bounds and fresh, convert it to rotten
                    if (nr not in range(rows) or nc not in range(cols) or grid[nr][nc] != 1):
                        continue 
                    grid[nr][nc] = 2
                    rotten.append([nr,nc])
                    # decrement number of fresh
                    fresh -= 1
            # increment time
            time += 1

        return time if fresh == 0 else -1

                
                


        