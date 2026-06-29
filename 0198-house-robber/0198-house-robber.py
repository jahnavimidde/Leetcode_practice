class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        # def helper(ind,dp):
        #     if  ind>len(nums)-1:
                
        #         return 0
        #     if dp[ind]!=-1:
        #         return dp[ind]
        #     else:
        #         take=nums[ind]+helper(ind+2,dp)
        #         nottake=helper(ind+1,dp)
        #         ans=max(take,nottake)
        #         dp[ind]=ans
        #         return dp[ind]
        # fs=helper(0,[-1]*(len(nums)))
        
        # return fs

        dp=[-1]*(len(nums)+2)
        n=len(nums)
        dp[n]=0
        dp[n+1]=0
        for i in range(n-1,-1,-1):
            dp[i]=max(dp[i+1],nums[i]+dp[i+2])
        return dp[0]
