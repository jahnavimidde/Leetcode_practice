class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """

#recursion 

        def helper(ind1,ind2,dp):
            if ind1==ind2:
                return 0
            if ind1>ind2:
                return 0
            else:
                if dp[ind1][ind2]!=0:
                    return dp[ind1][ind2]
                if s[ind1]==s[ind2]:
                    return helper(ind1+1,ind2-1,dp)
                else:
                    left_ins=helper(ind1,ind2-1,dp) #leetcode l and e are not matching then decide insertion l on right or e on left
                    right_ins=helper(ind1+1,ind2,dp)
                    dp[ind1][ind2]=1+min(left_ins,right_ins)
                    return 1+min(left_ins,right_ins)
        dp=[[0]*(len(s)+1) for _ in range(len(s)+1)]
        ans=helper(0,len(s)-1,dp)
        return ans

#space optimization with dp 
        #   prev=[0]*len(s)+1
        #   for i in range(len(s),0,-1):
        #     curr=[0]*len(s)+1
        #     for j in range(1,len(s)+1):
        #         if s[i-1]=s[j-1]:
        #             curr[j]=



                 
        