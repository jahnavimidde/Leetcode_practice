class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()  # Sort to handle duplicates
        result = []
        self.backtrack(0, nums, [], result)
        return result
        
    # Function to generate all unique subsets
    def backtrack(self, start, nums, current, result):
        # Add a copy of current subset
        result.append(list(current))

        # Iterate from 'start' index
        for i in range(start, len(nums)):
            # Skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue

            # Include nums[i]
            current.append(nums[i])

            # Recurse
            self.backtrack(i + 1, nums, current, result)

            # Backtrack
            current.pop()

    



