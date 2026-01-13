class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s="1"
        for j in range(2,n+1):
            next=""
            count=1
            for i in range(1,len(s)+1):
                if i<len(s) and s[i]==s[i-1]:
                    count+=1
                else:
                    next+=str(count)+s[i-1]
                    count=1
            s=next
        return s
        