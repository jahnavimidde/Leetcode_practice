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



#tabulation
        # dp = [[0] * (n) for _ in range(m)]

        # dp[m-1][n-1] = 1

        # for r in range(m-1, -1, -1):
        #     for d in range(n-1, -1, -1):
        #         if r == m-1 and d == n-1:
        #             continue

        #         right = dp[r][d+1] if d+1 < n else 0
        #         down = dp[r+1][d] if r+1 < m else 0

        #         dp[r][d] = right + down

        # return dp[0][0]


# space optimisation
# to compute the cell we only need prev cell and above cell  
# prev cell is obtained by current row,and above cell is obtained by maintaing the prev row values (that is 1D array)


#How many ways are there to reach the cell? (that is what each cell represents )  
        prev=[0]*n

        for i in range(m):
            temp=[-1 for _ in range(n)]
            for j in range(n):
                
                if i==0 and j==0:
                    temp[j]=1 #there is only one way to reach the start
                else:
                    above=prev[j] 
                    pre=temp[j-1] if j>0 else 0
                    temp[j]=above+pre
            prev=temp
        return temp[n-1]
        
                    





            
            
            
        
            
                
        