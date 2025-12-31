class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        first={}
        last={}
        for i,num in enumerate(nums):
            if num not in freq:
                freq[num]=1
                first[num]=i
            freq[num]+=1
            last[num]=i
        deg=max(freq.values())
        ans=len(nums)
        for num in freq:
            if freq[num]==deg:
                ans=min(ans,last[num]-first[num]+1)
        return ans
