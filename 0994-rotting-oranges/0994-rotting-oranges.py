from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        # Step 1: Find all rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0
        
        # Step 2: BFS
        while queue:
            r, c, time = queue.popleft()
            minutes = max(minutes, time)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Rot it
                    fresh -= 1
                    queue.append((nr, nc, time + 1))
        
        # Step 3: Check if all are rotten
        return minutes if fresh == 0 else -1
