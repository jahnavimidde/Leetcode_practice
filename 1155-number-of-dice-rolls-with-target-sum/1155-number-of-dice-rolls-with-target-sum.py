class Solution(object):
    def numRollsToTarget(self, n, k, target):
        dp = [[-1] * (target + 1) for _ in range(n + 1)]

        def helper(d, t):
            if d == 0:
                if t == 0:
                    return 1
                return 0

            
            if t < 0:
                return 0

            if dp[d][t] != -1:
                return dp[d][t]

            ways = 0

            for face in range(1, k + 1):
                ways += helper(d - 1, t - face)

            dp[d][t] = ways
            return ways

        return helper(n, target)%(10**9+7)