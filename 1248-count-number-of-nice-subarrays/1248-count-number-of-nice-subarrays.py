class Solution(object):
    def numberOfSubarrays(self, nums, goal):
        l = r = 0
        curr_sum = count = 0
        n = len(nums)

        return self.helper(l, r, curr_sum, count, n, goal, nums) - self.helper(l, r, curr_sum, count, n, goal - 1, nums)

    def helper(self, l, r, curr_sum, count, n, goal, nums):
        if goal < 0:
            return 0

        while r < n:
            #count of odd
            curr_sum += (nums[r])%2 #odd%2=1 else 0 added

            while curr_sum > goal:
                curr_sum -= (nums[l]%2) #odd%2=1 else 0 substracted
                l += 1

            count += (r - l + 1) #[1,1].. l at 0 r at 1..counting atleast k/k-1 odd means all conditions including k=0 1 ...k-1/k
            r += 1   

        return count   


        #exact k=atleast k-atleast k-1