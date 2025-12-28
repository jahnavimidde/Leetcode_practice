class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        p=1
        s=0
        for i in str(n):
            p*=int(i)
            s+=int(i)
        return p-s
        