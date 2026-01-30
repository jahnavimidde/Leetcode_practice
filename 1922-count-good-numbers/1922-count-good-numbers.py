class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD=10**9+7
        even =(n+1)//2
        odd=n//2
        return (self.pow(5,even,MOD)*self.pow(4,odd,MOD))%MOD
    def pow(self,base,exp,MOD):
        result=1
        base%=MOD
        while exp>0:
            if exp%2==1:
                result=(result*base)%MOD
            base=(base*base)%MOD
            exp=exp//2
        return result

