class Solution(object):
    def canPartitionKSubsets(self, nums, k):

        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k

        nums.sort(reverse=True)

        buckets = [0] * k

        def dfs(i):

            if i == len(nums):
                return True

            for j in range(k):

                if buckets[j] + nums[i] <= target:

                    buckets[j] += nums[i]

                    if dfs(i + 1):
                        return True

                    buckets[j] -= nums[i]

                # Pruning: don't try other empty buckets with the same state
                if buckets[j] == 0:
                    break

            return False

        return dfs(0)