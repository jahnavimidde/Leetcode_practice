class Solution:
    def canAliceWin(self, nums):
        single_sum = 0
        double_sum = 0

        for num in nums:
            if num < 10:
                single_sum += num
            else:
                double_sum += num

        total_sum = sum(nums)

        # Alice chooses single-digit numbers
        if single_sum > total_sum - single_sum:
            return True

        # Alice chooses double-digit numbers
        if double_sum > total_sum - double_sum:
            return True

        return False
