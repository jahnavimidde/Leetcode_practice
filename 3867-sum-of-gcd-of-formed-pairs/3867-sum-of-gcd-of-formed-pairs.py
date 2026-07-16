from math import gcd

class Solution:
    def gcdSum(self, nums):
        prefix = []
        mx = 0

        for x in nums:
            mx = max(mx, x)
            prefix.append(gcd(x, mx))

        prefix.sort()

        ans = 0
        i = 0
        j = len(prefix) - 1

        while i < j:
            ans += gcd(prefix[i], prefix[j])
            i += 1
            j -= 1

        return ans
        