class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        words.sort(key=len)
        n = len(words)

        dp = [1] * n

        def isPred(a, b):
            if len(b) != len(a) + 1:
                return False

            i = j = 0

            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                j += 1

            return i == len(a)

        for ind in range(n):
            for prev in range(ind):
                if isPred(words[prev], words[ind]):
                    dp[ind] = max(dp[ind], dp[prev] + 1)

        return max(dp)