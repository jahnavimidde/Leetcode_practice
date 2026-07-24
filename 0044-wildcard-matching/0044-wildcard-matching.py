class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # def helper(ind1,ind2,dp):
        #     # if ind1==len(s) and ind2==len(p):
        #     #     dp[ind1][ind2]=True
        #     #     return True
            
            
        #     # if ind2==len(p):
        #     #     dp[ind1][ind2]=False
        #         # return False
        #     # if ind1 == len(s):
        #     #     while ind2< len(p):
        #     #         if p[ind2] != '*':
        #     #             dp[ind1][ind2]=False
        #     #             return False
        #     #         ind2 += 1
        #     #     dp[ind1][ind2]=True
        #     #     return True
            
            
            

        #     # if dp[ind1][ind2]!=-1:
        #     #     return dp[ind1][ind2]
        #     # match=False
            
            
        #     # one_match=False

        #     # zero_more=False

        #     if s[ind1]==p[ind2]:
        #         match=helper(ind1+1,ind2+1,dp)
        #     else:
                
        #         if p[ind2]=="?":
        #             one_match=helper(ind1+1,ind2+1,dp)
                
        #         if p[ind2]=="*":
        #             zeromatch=helper(ind1,ind2+1,dp)
                    
        #             allmatch=helper(ind1+1,ind2,dp)
        #             zero_more=zeromatch  or allmatch
        #     dp[ind1][ind2]=match or one_match or zero_more
        #     return match or one_match or zero_more
        # dp=[[-1 for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        # ans=helper(0,0,dp)
        # return ans

        n = len(s)
        m = len(p)

        dp = [[False]*(m+1) for _ in range(n+1)]

        dp[0][0] = True

        
        for j in range(1, m+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]

        for i in range(1, n+1):
            for j in range(1, m+1):

                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]

                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]

        return dp[n][m]
        

            

        
         
        
            



                

    
                    
                    
                
            
            
        