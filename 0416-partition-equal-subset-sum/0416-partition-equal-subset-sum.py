class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)

        if total % 2 != 0:
            return False

        target_ = total // 2

        prev = [False] * (target_ + 1)
        prev[0]=True
        if nums[0] <= target_:
           prev[nums[0]] = True
        
        

        
        for ind in range(1,len(nums)):
            curr=[False]* (target_ + 1)
            curr[0]=True
            for target in range(1,target_+1):
            
                t=False

                if target>=nums[ind]: 
                   t=prev[target-nums[ind]]
                nt=prev[target]
                curr[target]= nt or t
            prev=curr
        return prev[target_]
                