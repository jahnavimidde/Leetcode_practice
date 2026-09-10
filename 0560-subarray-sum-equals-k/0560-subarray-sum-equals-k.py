class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix1=0
        subarray=0
        i=0
        d={}
        d[0]=1
        while i<len(nums):
            prefix1+=nums[i]
            prefix2=prefix1-k
            
            if prefix2 in d:
                subarray+=d[prefix2]
            d[prefix1] = d.get(prefix1, 0) + 1

            i+=1
        
            
            
        return subarray

