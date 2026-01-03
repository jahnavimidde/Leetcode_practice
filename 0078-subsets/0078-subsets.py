class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        subset=1<<n # 2**n
        ans=[]
        for num in range(subset): # from 0 to subset
            list=[]
            for i in range(n): # check each bit in num 
                if num&(1<<i): # if ith bit in  num is 1 then append ith bit in list
                    list.append(nums[i])
            ans.append(list)
        return ans