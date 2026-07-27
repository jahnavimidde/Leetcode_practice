class Solution(object):
    def largestInteger(self, n, s):
        """
        :type n: int
        :type s: int
        :rtype: int
        """
        if s > 9 * n:
            return -1

        ans = []

        for i in range(n):
            digit = min(9, s)
            ans.append(str(digit))
            s -= digit

        return int("".join(ans))