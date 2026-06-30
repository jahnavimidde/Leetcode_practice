class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1]=1

        def helper(r,d,dp):
            if r>m-1:
                return 0
            if d>n-1:
                return 0

            if dp[r][d]!=-1:
                return dp[r][d]
            

            
            right=helper(r+1,d,dp)
            down=helper(r,d+1,dp)
            dp[r][d]=right+down
            return dp[r][d]
        ans=helper(0,0,dp)
        return ans
            
                
        