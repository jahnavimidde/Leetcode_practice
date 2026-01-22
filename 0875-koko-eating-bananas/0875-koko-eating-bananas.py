import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2
            total = self.helper(piles, mid)

            if total <= h:
                high = mid - 1   # try smaller speed
            else:
                low = mid + 1    # need faster speed

        return low

    def helper(self, arr, mid):
        total = 0
        for bananas in arr:
            total += (bananas + mid - 1) // mid
        return total
