class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        nge = [-1] * n  
        stack = []

        for i in range(2*n - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()

            if i < n:
                if stack:
                    nge[i] = stack[-1]

            stack.append(nums[i % n])

        return nge