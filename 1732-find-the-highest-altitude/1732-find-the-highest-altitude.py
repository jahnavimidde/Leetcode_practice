class Solution(object):
    def largestAltitude(self, gain):
        curr = 0
        ans = 0

        for g in gain:
            curr += g
            ans = max(ans, curr)

        return ans