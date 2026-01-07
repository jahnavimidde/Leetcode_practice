class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        #optimal solution ..see in notebook 
        while right>left:
            right=right&(right-1)
        return right