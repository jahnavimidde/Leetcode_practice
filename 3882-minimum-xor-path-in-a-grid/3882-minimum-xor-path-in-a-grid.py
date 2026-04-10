class Solution(object):
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[set() for i in range(n)] for j in range(m)]

        dp[0][0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                for val in dp[i][j]:
                    if i + 1 < m:
                        dp[i+1][j].add(val ^ grid[i+1][j])
                    if j + 1 < n:
                        dp[i][j+1].add(val ^ grid[i][j+1])

        return min(dp[m-1][n-1])