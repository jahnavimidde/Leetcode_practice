class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxcount=0
        count1=0
        
        for i in s:
            if i=='(':
                count1+=1
                maxcount=max(count1,maxcount)
            elif i==')':
                count1-=1
        return maxcount
            
        