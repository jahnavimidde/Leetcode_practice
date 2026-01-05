class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #sort array 1 1 1 2 2 2 3 4 4 4 check at index 1 compare before ele 
        # if same or not.  same ? move to next index+3 pos and check .else return index-1
        # edge cases if element at last we cant find it so after loop end we simply return last . 
        nums.sort()
        low=1
        high=len(nums)-1
        while low<=high:
            if nums[low]==nums[low-1]:
                low+=3
            else:
                return nums[low-1]
        return nums[high]