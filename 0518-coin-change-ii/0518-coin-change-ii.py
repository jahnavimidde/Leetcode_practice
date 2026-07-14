class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # if amount==0:
        #     return 0
        # if len(coins)==1 and amount%coins[0]!=0:
        #     return -1
        # if len(coins)==1 and coins[0]>amount:
        #     return -1
        # prev=[-1 for _ in range(amount + 1)]
        
        # for i in range(amount+1):
        #     if i%coins[0]==0:
        #        prev[i]=i//coins[0]
        #     else:
        #         prev[i]=0
        # for i in range(1,len(coins)):
        #     curr=[0 for _ in range(amount+1)]
        #     curr[0]=0
        #     for j in range(1,amount+1):
                
        #         nt=prev[j]
        #         t=0
        #         if coins[i] <= j:
        #            t=curr[j-coins[i]]
        #         curr[j]=
        #     prev=curr
        # ans = prev[amount]
        # return -1 if ans``


   
        if amount==0:
            return 1
        if len(coins)==1 and amount%coins[0]!=0:
            return 0
        if len(coins)==1 and coins[0]>amount:
            return 0
        
        def helper(ind,total,dp):
            
            
            if ind<0:
            
                return 0
            if total==0:
                return 1
            
            if ind==0 and total%coins[ind]==0:
                dp[ind][total]=1
                return 1
            if dp[ind][total]!=-1:
                return dp[ind][total]
            nt=helper(ind-1,total,dp)
            
            t=0
            
                
                
            if coins[ind] <= total:
              t=helper(ind,total-coins[ind],dp)
            dp[ind][total]=nt+t
            return nt+t
        dp=[[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        ans=helper(len(coins)-1,amount,dp)
        return ans

        
        