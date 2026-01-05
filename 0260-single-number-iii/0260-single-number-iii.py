class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # brute firce frequecy count
        #optimal is using Xor     
        #1.do xor for all numbers ,o you get xor of unique numbers (3,5 in example)   101 ^011 means 110 . the 0th bits are same in (5,3)  1 and 2nd bits are diffrent .
        #intution ...make buckets of 2    b1 and b2 
        #b1 contains 1st bit is set and b2 contains 1st is unset .so 3 and 5 are seperated xor the elements ib b1 and b2 ...at end only 5 and 3 will be present 
        xorr=0
        for num in nums:
            xorr=xorr^num
        rightmost=(xorr&(xorr-1))^xorr  #give the right most bit which uniques numbers are diffrent at 
        b1=0
        b2=0
        for i in range(len(nums)):
            if nums[i]&rightmost:
                b1=b1^nums[i]
            else:
                b2=b2^nums[i]
        return [b1,b2]
        