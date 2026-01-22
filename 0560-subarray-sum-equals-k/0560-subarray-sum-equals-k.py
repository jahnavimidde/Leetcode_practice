class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        map={}
        map[0]=1
        current_sum=0
        subarray=0
        for i in range(len(nums)):
            current_sum+=nums[i]
            diff=current_sum - k 
            if diff  in map:
                subarray+=map[diff]
            if current_sum not in map:
                map[current_sum]=1
            else:
                map[current_sum]+=1
            
            
        return subarray


        