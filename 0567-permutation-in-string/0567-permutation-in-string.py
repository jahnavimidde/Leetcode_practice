class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #fixed window with k ele with hash
        d={}
        for i in s1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        k=len(s1)
        window={}
        l=0
        r=0
        while r<len(s2):
            
            # check l-r+1 and   window and d are same
            window[s2[r]]=window.get(s2[r],0)+1
            if r-l+1>k:
                window[s2[l]]-=1
                if window[s2[l]]==0:
                    del window[s2[l]]
                l+=1
            if r-l+1==k and d==window:
                return True
            r+=1

            
        return False
            


        