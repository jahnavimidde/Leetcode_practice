class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp = [[-1 for _ in range(n)] for _ in range(m)]
        # dp[m-1][n-1]=1

        # def helper(r,d,dp):
        #     if r>m-1:
        #         return 0
        #     if d>n-1:
        #         return 0

        #     if dp[r][d]!=-1:
        #         return dp[r][d]
            

            
        #     right=helper(r+1,d,dp)
        #     down=helper(r,d+1,dp)
        #     dp[r][d]=right+down
        #     return dp[r][d]
        # ans=helper(0,0,dp)
        # return ans




        dp = [[0] * n for _ in range(m)]

        dp[m-1][n-1] = 1

        for r in range(m-1, -1, -1):
            for d in range(n-1, -1, -1):
                if r == m-1 and d == n-1:
                    continue

                right = dp[r][d+1] if d+1 < n else 0
                down = dp[r+1][d] if r+1 < m else 0

                dp[r][d] = right + down

        return dp[0][0]


            
            
            
        
            
                
        