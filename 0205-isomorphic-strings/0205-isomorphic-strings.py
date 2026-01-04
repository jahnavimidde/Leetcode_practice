class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        d1 = {}
        d2 = {}

        for i in range(len(s)):
            if s[i] in d1 and d1[s[i]] != t[i]:
                return False
            if t[i] in d2 and d2[t[i]] != s[i]:
                return False

            d1[s[i]] = t[i]
            d2[t[i]] = s[i]

        return True
