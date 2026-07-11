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
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0]=0
        for i in range(amount+1):
            if i%coins[0]==0:
               dp[0][i]=i//coins[0]
            else:
                dp[0][i]=float('inf')
        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                
                nt=dp[i-1][j]
                t=float('inf')
                if coins[i] <= j:
                   t=1+dp[i][j-coins[i]]
                dp[i][j]=min(t,nt)
        ans = dp[len(coins)-1][amount]
        return -1 if ans == float('inf') else ans
        
        

        
                

        

        