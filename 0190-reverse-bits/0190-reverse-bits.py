class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        for _ in range(32): #32 bits
            ans=(ans<<1)|(n&1) #n&1 returns  the right most bit(evry time ans is shifted to left side and or adds the rightmost bit)
            n=n>>1  # move bits to right means 1101 then  110
        return ans
        