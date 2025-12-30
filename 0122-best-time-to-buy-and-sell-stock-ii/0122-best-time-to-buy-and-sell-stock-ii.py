class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        s=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                s+=prices[i]-prices[i-1]
        return s

