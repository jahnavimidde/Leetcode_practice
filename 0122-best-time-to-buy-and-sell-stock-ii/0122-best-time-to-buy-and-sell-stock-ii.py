class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def helper(ind,buy,dp):
            if ind==len(prices):
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            take=0
            nottake=0
            sell=0
            notsell=0

            if buy: #if buy==1 it means there are no stocks in hand which are bought
                take= -(prices[ind])+helper(ind+1,0,dp)
                nottake=helper(ind+1,1,dp)

            else: 
                #if stocks are bought then sell (sell,notsell)
                sell=prices[ind]+helper(ind+1,1,dp)
                notsell=helper(ind+1,0,dp)
            dp[ind][buy]=max(take,nottake,sell,notsell)
            return max(take,nottake,sell,notsell)
        dp=[[-1 for _ in range(2)] for _ in range(len(prices))]
        ans=helper(0,1,dp)
        return ans


