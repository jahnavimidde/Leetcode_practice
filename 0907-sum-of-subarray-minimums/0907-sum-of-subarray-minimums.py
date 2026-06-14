class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        n = len(arr)

        # NSE
        stack = []
        NSE = [n] * n

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                NSE[i] = stack[-1]

            stack.append(i)

        # PSE
        stack = []
        PSE = [-1] * n

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                PSE[i] = stack[-1]

            stack.append(i)

        total = 0

        for i in range(n):
            nse = NSE[i]
            pse = PSE[i]

            left = i - pse
            right = nse - i

            total += left * right * arr[i]

        return total % (10**9 + 7)