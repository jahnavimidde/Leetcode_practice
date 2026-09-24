class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if (mid==0 or nums[mid-1]<nums[mid]) and (mid==len(nums)-1 or nums[mid+1]<nums[mid]):
                return mid 
            elif nums[mid-1]<nums[mid] or mid==0:
                low=mid+1   #         left side:   maybe a peak
# right side:  definitely a peak
            else:
                high=mid-1

        