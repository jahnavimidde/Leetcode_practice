class Solution(object):
    def trap(self, height):
        l, r = 0, len(height) - 1
        lmax = rmax = 0
        total = 0

        while l < r:

            if height[l] < height[r]:

                if height[l] >= lmax:
                    lmax = height[l]
                else:
                    total += lmax - height[l]

                l += 1

            else:

                if height[r] >= rmax:
                    rmax = height[r]
                else:
                    total += rmax - height[r]

                r -= 1

        return total