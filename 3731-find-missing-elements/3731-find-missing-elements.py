class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mini=min(nums)
        maxi=max(nums)
        arr=[]
        for i in range(mini,maxi+1):
            if i not in nums:
                arr.append(i)
        return arr