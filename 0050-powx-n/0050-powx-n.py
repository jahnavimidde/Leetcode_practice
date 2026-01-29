class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result=1
        if n<0:
            x=1/x
            n=-n
        if n==0:
            return 1 
        res=self.helper(result,n,x)
        return res
    def helper(self,result,n,x):
        if n<=0:
            return result
        if n%2==1:
            result=result*x
        x=x*x
        n=n//2
        return self.helper(result,n,x)
            
        