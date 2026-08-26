class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums,ds,ans,map):
            if len(ds)==len(nums):
                ans.append(list(ds))
                return 
            for i in range(len(nums)):
                if map[i]!=1:
                    ds.append(nums[i])
                    map[i]=1
                    helper(nums,ds,ans,map)
                    ds.pop()
                    map[i]=-1
        ans=[]
        map=[-1]*len(nums)
        helper(nums,[],ans,map)
        return ans 
        
        
        