class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0
        if len(coins)==1 and amount%coins[0]!=0:
            return -1
        if len(coins)==1 and coins[0]>amount:
            return -1
        def helper(ind,total,dp):
            
            
            if ind<0:
                return float('inf')
            if total==0:
                return 0
            
            if ind==0 and total%coins[ind]==0:
                return total//coins[ind]
            if dp[ind][total]!=-1:
                return dp[ind][total]
            
            nt=helper(ind-1,total,dp)
            
            t=float('inf')
            
                
                
            if coins[ind] <= total:
              t=1+helper(ind,total-coins[ind],dp)
            
            dp[ind][total]=min(t,nt)
            return dp[ind][total]
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0]=0
        for i in range(amount+1):
            if i%coins[0]==0:
               dp[0][i]=i//coins[0]
        ans = helper(len(coins)-1, amount, dp)

        if ans == float('inf'):
            return -1
        return ans
                

        

        