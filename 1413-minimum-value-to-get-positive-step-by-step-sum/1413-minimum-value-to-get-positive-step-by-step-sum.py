class Solution(object):
    def minStartValue(self, nums):
        total = 0
        min_sum = 0

        for num in nums:
            total += num
            min_sum = min(min_sum, total)

        return 1 - min_sum