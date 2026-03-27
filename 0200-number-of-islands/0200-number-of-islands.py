from collections import deque

class Solution(object):
    def numIslands(self, grid):

        n = len(grid)
        m = len(grid[0])

        vis = [[0]*m for _ in range(n)]
        count = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            vis[r][c] = 1

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nrow = row + dr
                    ncol = col + dc

                    if (0 <= nrow < n and 0 <= ncol < m and
                        grid[nrow][ncol] == '1' and vis[nrow][ncol] == 0):

                        vis[nrow][ncol] = 1
                        q.append((nrow, ncol))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and vis[i][j] == 0:
                    count += 1
                    bfs(i, j)

        return count