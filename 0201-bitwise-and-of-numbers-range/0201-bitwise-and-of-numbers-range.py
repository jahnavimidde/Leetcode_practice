class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        #right shift the nums until they are equal .because if the bits in them differ means(0,1) AND of those bits will be zero..so count hoe many BITS GONNNA BE ZERO >>PADDING THE NO OF THE ZEROES BY LEFT SHIFTING AGAIN..SMART!
        count=0
        while left!=right:
            left=left>>1
            right=right>>1
            count+=1
        ans=left&right
        ans=ans<<count
        return ans
        