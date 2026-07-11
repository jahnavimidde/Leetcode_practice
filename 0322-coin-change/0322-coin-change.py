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
        prev=[-1 for _ in range(amount + 1)]
        
        for i in range(amount+1):
            if i%coins[0]==0:
               prev[i]=i//coins[0]
            else:
                prev[i]=float('inf')
        for i in range(1,len(coins)):
            curr=[-1 for _ in range(amount+1)]
            curr[0]=0
            for j in range(1,amount+1):
                
                nt=prev[j]
                t=float('inf')
                if coins[i] <= j:
                   t=1+curr[j-coins[i]]
                curr[j]=min(t,nt)
            prev=curr
        ans = prev[amount]
        return -1 if ans == float('inf') else ans
        
        

        
                

        

        