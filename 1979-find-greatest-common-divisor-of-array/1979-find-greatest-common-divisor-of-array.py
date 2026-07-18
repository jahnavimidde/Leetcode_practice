class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)

        while mx:
            mn, mx = mx, mn % mx

        return mn