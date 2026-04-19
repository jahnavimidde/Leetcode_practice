class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        def farthest_pos(target,left):
            low=left
            high=len(nums2)-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if nums2[mid]>=target:
                    ans=mid
                    low=mid+1
                else:
                    high=mid-1
            return ans
        maxi=0
        for i in range(len(nums1)):
            ans=farthest_pos(nums1[i],i)
            if ans!=-1:
                maxi=max(maxi,ans-i)
        return maxi
        