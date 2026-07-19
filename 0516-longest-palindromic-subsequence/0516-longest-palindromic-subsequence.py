class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev=[0]*(len(s)+1)
        maxi=0
        for i in range(len(s),0,-1):
            curr=[0]*(len(s)+1)
            for j in range(1,len(s)+1):
                if s[i-1]==s[j-1]:
                    curr[j]=1+prev[j-1]
                    maxi=max(maxi,curr[j])
                else:
                    curr[j]=max(prev[j],curr[j-1])
                    maxi=max(maxi,curr[j])
            prev=curr
        return maxi