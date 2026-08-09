class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for m in range(n, 0, -1):

                res = 0

                for x in range(1, 2 * m + 1):
                    if i + x > n:
                        break

                    next_m = max(m, x)

                    curr = suffix[i] - dp[i + x][next_m]

                    res = max(res, curr)

                dp[i][m] = res

        prev = dp[0][1]

        return prev