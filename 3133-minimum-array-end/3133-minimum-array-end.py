class Solution(object):
    def minEnd(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        v=n-1
        ans=x
        bit=0
        while v>0:
            if (x>>bit)&1==0:
                if v&1==1:
                    ans=ans|(1<<bit)
                v>>=1
            bit+=1
        return ans 

        