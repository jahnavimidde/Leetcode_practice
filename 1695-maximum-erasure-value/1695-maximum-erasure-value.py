class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        seen = set()

        left = 0
        curr_sum = 0
        ans = 0

        for right in range(len(nums)):

            # Remove duplicates
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            # Add current element
            seen.add(nums[right])
            curr_sum += nums[right]

            # Update maximum
            ans = max(ans, curr_sum)

        return ans