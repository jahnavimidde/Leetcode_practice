class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=r=0
        char=""
        max_size=0
        n=len(s)
        while r<n:
            while s[r] in char:
                char=char[1:]
                l+=1
            char+=s[r]
            max_size=max(max_size,r-l+1)
            r+=1
        return max_size
            