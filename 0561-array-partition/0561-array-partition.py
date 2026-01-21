class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_sum=0
        for i in range(len(nums)):
            if i%2==0:
                max_sum+=nums[i]
        return max_sum
        