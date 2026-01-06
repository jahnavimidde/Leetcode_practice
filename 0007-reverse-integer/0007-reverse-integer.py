class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pos=True
        if x<0:
            
            pos=False
            x*=-1
        sum=0
        while x>0:
            rem=x%10
            sum=sum*10+rem
            x=x//10
        if pos is False:
            sum*=-1
        if not -2**31<sum<2**31-1:
            return 0 
        return sum

        