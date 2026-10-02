class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        char = {}
        maxi = 0

        while r < len(s):
            if s[r]  in char:
                
                l = max(l, char[s[r]]+1)
                
            char[s[r]]=r
            maxi=max(maxi,r-l+1)
            r+=1

        return maxi