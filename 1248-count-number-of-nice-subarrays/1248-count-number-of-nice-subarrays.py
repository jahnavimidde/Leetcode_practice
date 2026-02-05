class Solution(object):
    def numberOfSubarrays(self, nums, goal):
        l = r = 0
        curr_sum = count = 0
        n = len(nums)

        return self.helper(l, r, curr_sum, count, n, goal, nums) - self.helper(l, r, curr_sum, count, n, goal - 1, nums)

    def helper(self, l, r, curr_sum, count, n, goal, nums):
        if goal < 0:
            return 0

        while r < n:
            curr_sum += (nums[r])%2

            while curr_sum > goal:
                curr_sum -= (nums[l]%2)
                l += 1

            count += (r - l + 1)
            r += 1   # ✅ move right pointer

        return count   # ✅ return AFTER loop
