class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def helper(ind1,ind2,dp):
            if ind1<0:
                return ind2+1   #if word1 exhausted then insert the all word2 chars
            if ind2<0:
                return ind1+1   #if word2 exhuasted we found our word2 then delete remaining word1
            match=float('inf')
            notmatch=float('inf')
            if dp[ind1][ind2]!=float('inf'):
                return dp[ind1][ind2]
            if word1[ind1]==word2[ind2]:
                match=helper(ind1-1,ind2-1,dp)

            
            else:
                delete=1+helper(ind1-1,ind2,dp)
                insert=1+helper(ind1,ind2-1,dp) #insert at ind1+1 and cancel with ind2 and move
                replace=1+helper(ind1-1,ind2-1,dp)
                notmatch=min(delete,insert,replace)
            dp[ind1][ind2]=min(match,notmatch)
            return min(match,notmatch)
        dp = [[float('inf') for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        return helper(len(word1)-1,len(word2)-1,dp)
        
    
                
        