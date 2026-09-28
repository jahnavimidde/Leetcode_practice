class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low=min(nums) #if nums have all same ele ,len(nums)==k we allocate the min(nums)
        high=sum(nums) # if k=1 then we dont need to split
        def possibility(arr,mid,k):
            s=1 
            sum_=0

            for i in range(len(arr)):
                if arr[i]>mid:
                    return False
                if sum_+arr[i]>mid:
                    s+=1 #splits
                    sum_=arr[i]
                else:
                    sum_+=arr[i]
                
            if s>k:
                return False  # unable to split the nums with this specific sum as maximum
            else:
                return True 

        while low<=high:
            mid=(low+high)//2
            if possibility(nums,mid,k):
                #check that mid can be an answer by not crossing the sum of any subarray by mid (mini) with a split of k
                ans=mid
                high=mid-1  # need to check mini 
            else:
                low=mid+1
        return ans 

