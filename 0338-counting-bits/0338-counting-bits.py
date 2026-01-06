class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        #011(3) 110(6) 3 is left shitfed and 7(111) 3 is left shifted and added 1 means-->the no of 1's in n will be equal to that of in n/2 (even)if it is odd 1's in n/2 +1
        ans = [0] * (n + 1)
        for i in range(n+1):
            
            if i&1==1: 
                #means n%2==1
                ans[i]=ans[i//2]+1
            else:
                ans[i]=ans[i//2]
        return ans


