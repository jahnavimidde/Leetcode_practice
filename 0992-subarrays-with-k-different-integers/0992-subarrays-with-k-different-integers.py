class Solution(object):
    # Helper function to count subarrays with at most K distinct integers
    def atMostK(self, nums, K):
        freq = {}
        left = 0
        count = 0

        for right in range(len(nums)):
            if nums[right] not in freq or freq[nums[right]] == 0:
                K -= 1

            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while K < 0:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    K += 1
                left += 1

            count += (right - left + 1)

        return count

    # Main function
    def subarraysWithKDistinct(self, nums, k):
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)