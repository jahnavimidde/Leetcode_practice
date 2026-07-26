class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # If you buy on day 1, sell on day 2, buy again on day 2, and then sell on some day x, your overall profit will be = (prices[x]-prices[2])+(prices[2]-prices[1]) = prices[x]-prices[1]. Thus, the operation on day 2 made no difference- you might as well just skip that transaction and just sell later on day x directly. So, it doesn't make sense to buy again on the same day as selling.


        def helper(ind,buy,cap,dp):
            
            if ind==len(prices) or cap==0:
                return 0
            if dp[ind][buy][cap]!=-1:
                return dp[ind][buy][cap]
            take=0
            nottake=0
            sell=0
            notsell=0

            if buy: #if buy==1 it means there are no stocks in hand which are bought
                take= -(prices[ind])+helper(ind+1,0,cap,dp)
                nottake=helper(ind+1,1,cap,dp)

            else: 
                #if stocks are bought then sell (sell,notsell)
                sell=prices[ind]+helper(ind+1,1,cap-1,dp)
                notsell=helper(ind+1,0,cap,dp)
            dp[ind][buy][cap]=max(take,nottake,sell,notsell)
            return max(take,nottake,sell,notsell)
        dp=[[[-1 for _ in range(3)]for _ in range(2)] for _ in range(len(prices))]
        ans=helper(0,1,2,dp)
        return ans



            