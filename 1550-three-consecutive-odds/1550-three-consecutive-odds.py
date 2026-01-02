class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c=0
        for i in arr:
            if i%2==1:
                c+=1
                if c==3:
                    return True
            else:
                 c=0
        return c==3
