class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # For every element, calculate NGE and PGE.
        # This gives the number of subarrays in which the element
        # acts as the maximum.

        # Also calculate NSE and PSE.
        # This gives the number of subarrays in which the element
        # acts as the minimum.

        # Contribution as maximum:
        # nums[i] * (# subarrays where nums[i] is maximum)

        # Contribution as minimum:
        # nums[i] * (# subarrays where nums[i] is minimum)

        # Answer = sum of maximum contributions
        #          - sum of minimum contributions

        n = len(nums)

        # NGE
        stack = []
        nge = [n] * n

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                nge[i] = stack[-1]

            stack.append(i)

        # PGE
        stack = []
        pge = [-1] * n

        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()

            if stack:
                pge[i] = stack[-1]

            stack.append(i)

        # NSE
        stack = []
        nse = [n] * n

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1]

            stack.append(i)

        # PSE
        stack = []
        pse = [-1] * n

        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()

            if stack:
                pse[i] = stack[-1]

            stack.append(i)


        totalMin = 0
        totalMax = 0

        for i in range(n):
            nextSmaller = nse[i]
            prevSmaller = pse[i]
            nextGreater = nge[i]
            prevGreater = pge[i]

            leftMin = i - prevSmaller
            rightMin = nextSmaller - i

            totalMin += leftMin * rightMin * nums[i]

            leftMax = i - prevGreater
            rightMax = nextGreater - i

            totalMax += leftMax * rightMax * nums[i]

        return totalMax - totalMin

            

        
