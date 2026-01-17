class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """



        """for i in s:
            if s.rindex(i)==s.index(i):
                return s.index(i)
        return -1"""
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1
        
