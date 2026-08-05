class Solution(object):
    def findNumberOfLIS(self, nums):
        n = len(nums)

        dp = [1] * n
        ct = [1] * n

        maxi = 1

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    ct[i] = ct[j]
                elif nums[j] < nums[i] and dp[j] + 1 == dp[i]:
                    ct[i] += ct[j]

            maxi = max(maxi, dp[i])

        return sum(ct[i] for i in range(n) if dp[i] == maxi)