class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        res=""
        for i in range(len(nums)):
            bit=nums[i][i]
            if bit=='0':
                bit='1'
            else:
                bit='0'
            res+=bit
        return res
