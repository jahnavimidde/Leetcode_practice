class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        def helper(i, j, s, t, dp):
            # If matched all chars of t
            if j == len(t):
                return 1

            # If we have exhausted s but not t
            if i == len(s):
                return 0

        
            if dp[i][j] != -1:
                return dp[i][j]

            
            if s[i] == t[j]:
            
                take = helper(i + 1, j + 1, s, t, dp)

                
                notTake =helper(i + 1, j, s, t, dp)

                
                dp[i][j] = take + notTake
            else:
                # If mismatch, skip char of s
                dp[i][j] = helper(i + 1, j, s, t, dp)

            return dp[i][j]

        
        dp = [[-1] * len(t) for _ in range(len(s))]

            
        return helper(0, 0, s, t, dp)
        

        
        
        