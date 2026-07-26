class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # def helper(ind,buy,dp):
        #     if ind==len(prices):
        #         return 0
        #     if dp[ind][buy]!=-1:
        #         return dp[ind][buy]
        #     take=0
        #     nottake=0
        #     sell=0
        #     notsell=0

        #     if buy: #if buy==1 it means there are no stocks in hand which are bought
        #         take= -(prices[ind])+helper(ind+1,0,dp)
        #         nottake=helper(ind+1,1,dp)

        #     else: 
        #         #if stocks are bought then sell (sell,notsell)
        #         sell=prices[ind]+helper(ind+1,1,dp)
        #         notsell=helper(ind+1,0,dp)
        #     dp[ind][buy]=max(take,nottake,sell,notsell)
        #     return max(take,nottake,sell,notsell)
        # dp=[[-1 for _ in range(2)] for _ in range(len(prices))]
        # ans=helper(0,1,dp)
        # return ans

        dp=[[-1 for _ in range(2)] for _ in range(len(prices)+1)]
        dp[len(prices)][0]=0
        dp[len(prices)][1]=0
        take=0
        nottake=0
        sell=0
        notsell=0
        for i in range(len(prices)-1,-1,-1):
            for j in range(1,-1,-1):
                if j==1:
                    take=-prices[i]+dp[i+1][0]
                    nottake=dp[i+1][1]
                    profit=max(take,nottake)
                else:
                    sell= prices[i]+dp[i+1][1]
                    notsell=dp[i+1][0]
                    profit=max(sell,notsell)
                dp[i][j]=profit
                
        return dp[0][1]

        


