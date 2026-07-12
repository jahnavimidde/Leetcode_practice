class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
       
        if sum(nums)< abs(target):
            return 0
        if (sum(nums)-target)%2!=0: #equation   note 
            return 0
        if len(nums)==1:
            if nums[0]==0 :
                 
                return 2 if target==0 else 0
            return 1 if abs(nums[0])==abs(target) else 0
                
            
           
        # def helper(ind,tar,dp):
            
        #     if ind==0:
        #         if nums[0]==0 and tar==0:
        #             return 2
        #         elif nums[0]==tar or tar==0:
        #             return 1
        #         else:
        #             return 0
        #     if dp[ind][tar]!=-1:
        #         return dp[ind][tar]

            # nt=helper(ind-1,tar,dp)
            # t=0
            # if tar>=nums[ind]:
            #     t=helper(ind-1,tar-nums[ind],dp)
            # dp[ind][tar]=t+nt
            # return dp[ind][tar]


        tar=(sum(nums)-target)//2 
        prev =[-1 for _ in range(tar+1)]
        for j in range(tar+1):
            
            if nums[0]==0 and j==0:
                prev[j]=2
            elif nums[0]==j or j==0:
                prev[j]=1
            else:
                prev[j]=0
        for i in range(1,len(nums)):
            curr=[-1 for _ in range(tar+1)] 
            for j in range(tar+1):
                nt=prev[j]
                t=0
                if j>=nums[i]:
                    t=prev[j-nums[i]]
                curr[j]=nt+t
            prev=curr

            
                
            
           

        
        return prev[tar]
            

        
        
        
        