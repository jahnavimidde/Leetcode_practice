class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res=x^y
        count=0
        while res:
            res=res&(res-1)
            count+=1
        return count
        