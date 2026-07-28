class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

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
        dp=[[[-1 for _ in range(k+1)]for _ in range(2)] for _ in range(len(prices))]
        ans=helper(0,1,k,dp)
        return ans
        