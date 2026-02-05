class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen=[-1,-1,-1]
        r=l=0
        n=len(s)
        count=0
        while r<n:
            last_seen[ord(s[r])-ord('a')]=r
            if not last_seen[0]==-1 and not last_seen[1]==-1 and not last_seen[2]==-1 :
                count+=(1+min( last_seen[0],last_seen[1],last_seen[2]))
            r+=1       
        return count