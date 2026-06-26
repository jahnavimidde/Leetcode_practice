class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return

        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (
                    i == 0 or i == len(grid)-1 or
                    j == 0 or j == len(grid[0])-1
                ):
                    grid[i][j] = 'T'      # Mark immediately
                    queue.append((i, j))

        dir = [(-1,0), (0,-1), (1,0), (0,1)]

        while queue:
            row, col = queue.popleft()

            for r, c in dir:
                nr = row + r
                nc = col + c

                if (0 <= nr < len(grid) and
                    0 <= nc < len(grid[0]) and
                    grid[nr][nc] == 1):

                    grid[nr][nc] = 'T'    # Mark before pushing
                    queue.append((nr, nc))
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    count+=1
        return count