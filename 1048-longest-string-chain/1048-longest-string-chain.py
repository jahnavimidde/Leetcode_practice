class Solution(object):
    def longestStrChain(self, words):

        words.sort(key=len)
        n = len(words)

        dp = [[-1 for _ in range(n + 1)] for _ in range(n)]

        def isPred(a, b):
            if len(b) != len(a) + 1:
                return False

            i = j = 0

            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                j += 1

            return i == len(a)

        def helper(ind, prev):

            if ind == n:
                return 0

            if dp[ind][prev + 1] != -1:
                return dp[ind][prev + 1]

            nottake = helper(ind + 1, prev)

            take = 0
            if prev == -1 or isPred(words[prev], words[ind]):
                take = 1 + helper(ind + 1, ind)

            dp[ind][prev + 1] = max(take, nottake)
            return dp[ind][prev + 1]

        return helper(0, -1)