class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        for i in range(n,101):
            product=1
            for s in str(i):
                product*=int(s)
            if product%t==0:
                return i
        