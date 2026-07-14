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


        if len(coins)<0:
            return 0
        if amount==0:
            return 1
        if len(coins)==1 and amount%coins[0]!=0:
            return 0
        if len(coins)==1 and coins[0]>amount:
            return 0
        
      
            
            
            
            
            
            
            

        prev=[-1 for _ in range(amount+1)] 
        
        for amount in range(amount+1):
            if amount%coins[0]==0:
                prev[amount]=1
            elif amount==0:
                prev[amount]=1
            elif amount%coins[0]!=0:
                prev[amount]=0
            elif coins[0]>amount:
                prev[amount]=0

        for ind in range(1,len(coins)):
            curr=[-1 for _ in range(amount+1)] 
            curr[0]=1
            for amount in range(amount+1):
                nt=prev[amount]
                t=0
                if coins[ind]<=amount:
                    t=curr[amount-coins[ind]]
                curr[amount]=t+nt
            prev=curr
        return prev[amount]


       

        

        
        