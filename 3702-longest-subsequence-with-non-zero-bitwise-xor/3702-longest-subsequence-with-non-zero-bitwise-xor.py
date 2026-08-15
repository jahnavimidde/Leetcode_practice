class Solution(object):
    def longestSubsequence(self, nums):
        n = len(nums)

        xor = 0
        zero = 0

        for x in nums:
            xor ^= x

            if x == 0:
                zero += 1

        if xor != 0:
            return n

        if zero == n:
            return 0

        return n - 1