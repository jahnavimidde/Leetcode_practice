class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)

        # Create DP table to store lengths of LCS for all substrings
        prev =[0] * (m + 1) 

        # Fill dp table bottom-up
        maxi=0
        for i in range(1, n + 1):
            curr=[0] * (m + 1) 
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    
                    curr[j] = 1 + prev[j - 1]
                    maxi=max(maxi,curr[j])
            prev=curr
        
        
        return maxi
        