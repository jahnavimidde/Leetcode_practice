class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        def helper(nums):
            next1 = 0
            next2 = 0
            n=len(nums)
            for i in range(n - 1, -1, -1):
                curr = max(next1, nums[i] + next2)
                next2 = next1
                next1 = curr

            return next1
        a=helper(nums[1:])
        b=helper(nums[0:len(nums)-1])
        return max(a,b)