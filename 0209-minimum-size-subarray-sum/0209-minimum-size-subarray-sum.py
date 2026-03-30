class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=0
        w_sum=0
        
        mini=float('inf')
        while right<=len(nums)-1 :
            
            w_sum+=nums[right]
            right+=1
            while w_sum>=target:
                mini=min(right-left,mini)
                w_sum-=nums[left]
                left+=1
                
            
            
        return mini if mini!=float('inf') else 0
        

            

