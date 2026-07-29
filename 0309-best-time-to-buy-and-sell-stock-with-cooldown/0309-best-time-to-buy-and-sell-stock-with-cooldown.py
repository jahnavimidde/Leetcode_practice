class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]

        def helper(ind, buy):
            if ind >= n:
                return 0

            if dp[ind][buy] != -1:
                return dp[ind][buy]

            if buy == 0:
                
                profit = max(
                    helper(ind + 1, 0),
                    -prices[ind] + helper(ind + 1, 1)
                )
            else:
                # cooldown for one day
                profit = max(
                    helper(ind + 1, 1),
                    prices[ind] + helper(ind + 2, 0)
                )

            dp[ind][buy] = profit
            return profit

        return helper(0, 0)