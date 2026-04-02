class Solution(object):

    def atMostK(self, nums, K):
        freq = {}
        left = 0
        count = 0
        k = K   # avoid modifying original

        for right in range(len(nums)):
            if nums[right] not in freq or freq[nums[right]] == 0:
                k -= 1

            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while k < 0:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    k += 1
                left += 1

            count += (right - left + 1)

        return count

    def countCompleteSubarrays(self, nums):
        k = len(set(nums))
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)