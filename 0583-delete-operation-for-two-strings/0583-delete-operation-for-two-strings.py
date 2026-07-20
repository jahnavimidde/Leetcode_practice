class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        def helper(nums1,nums2):
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
                    else:
                        curr[j]=max(curr[j-1],prev[j])
                        maxi=max(curr[j],maxi)
                prev=curr
            
            
            return maxi
        lcs=helper(word1,word2)
        w1=len(word1)-lcs
        w2=len(word2)-lcs
        return w1+w2
        

        