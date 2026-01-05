class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #better solution 
        #count te i th bit of each number check if i th bit in each num is multiple of three ....means [5,5,5,2,4,4,4]
        #101
        #101
        #101
        #010
        #100
        #100   by checking 0th bit of 5 2 4 there are 3 one bits then single number 0th bit is '0' like wise we need to do for 1 and 2 bit also 
        ans=0
        for bitindex in range(0,32):
            count=0
            for num in nums:
                
                if num &(1<<bitindex):
                    count+=1
            if count%3==1:
                    ans=ans|(1<<bitindex)
        if ans>=2**31:
            ans-=2**32
        return ans 
                    
