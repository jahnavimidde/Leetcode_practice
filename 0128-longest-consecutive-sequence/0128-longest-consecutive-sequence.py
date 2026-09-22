class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        arr=set(nums)
        maxi=0
        for i in arr:
            x=i
            cnt=1
            if x-1 not in arr:
                
                while x+1 in arr:
                    cnt+=1
                    x+=1
            maxi=max(cnt,maxi)
        return maxi
        