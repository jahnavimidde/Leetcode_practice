class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """ maintain count for 0 in window and store the index of zero . when extra zero appears take the first 0's index and continue from next index+1 to current zero,expand till no zero occurs ..if next zero occrs ..update window with index (of first zero in window)+1 to current pos """
        l=r=0
        count_z=0
        max_len=0
        index_z=[]
        n=len(nums)
        while r<n:
            if nums[r]==0:
                
                    count_z+=1
                    index_z.append(r)
            if count_z>k:
                
                    l=index_z[0]+1
                    index_z=index_z[1:]
                    count_z-=1
            max_len=max(max_len,r-l+1)
            r+=1
        return max_len
        