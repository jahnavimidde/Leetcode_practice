class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #recursion

        # def helper(r,d):
        #     if r==len(grid)-1 and d==len(grid[0])-1:
        #         return grid[r][d]
            
        #     if r>=len(grid) or d>=len(grid[0]):
        #         return float('inf')
            
            

        #     right=grid[r][d]+helper(r,d+1)
        #     down=grid[r][d]+helper(r+1,d)
        #     return min(right,down)
        # mini=helper(0,0)
        # return mini

        dp = [[-1] * len(grid[0]) for _ in range(len(grid))]

        def helper(r, d):
            if r == len(grid)-1 and d == len(grid[0])-1:
                return grid[r][d]

            if r >= len(grid) or d >= len(grid[0]):
                return float('inf')

            if dp[r][d] != -1:
                return dp[r][d]

            right = helper(r, d+1)
            down = helper(r+1, d)

            dp[r][d] = grid[r][d] + min(right, down)
            return dp[r][d]

        return helper(0, 0)
            
        

        