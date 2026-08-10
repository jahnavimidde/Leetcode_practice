class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """

        cuts.append(n)
        cuts.insert(0, 0)
        cuts.sort()

        c = len(cuts) - 2 
        dp = [[0] * (c + 2) for _ in range(c + 2)]

        for i in range(c, 0, -1):
            for j in range(i, c + 1):
                mini = float('inf')
                for ind in range(i, j + 1):
                    
                    ans = cuts[j + 1] - cuts[i - 1] + dp[i][ind - 1] + dp[ind + 1][j]

                    mini = min(mini, ans)

               
                dp[i][j] = mini

        
        return dp[1][c]
        