class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res=[]
        if k==1 or len(nums)==1:
            return nums
        
        dq=deque()
        
        for i in range(len(nums)):
            
            
            while dq and nums[dq[-1]]<=nums[i]:
                dq.pop()
            dq.append(i)
            while dq and dq[0]<i-k+1:
                dq.popleft()
            
            if i>k-2:
                
                res.append(nums[dq[0]])
            
        return res

