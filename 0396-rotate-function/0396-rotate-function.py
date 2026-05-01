class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        
        total_sum = sum(nums)
        
        # F(0)
        f = sum(i * nums[i] for i in range(n))
        
        ans = f
        
        for k in range(1, n):
            f = f + total_sum - n * nums[n - k]
            ans = max(ans, f)
        
        return ans