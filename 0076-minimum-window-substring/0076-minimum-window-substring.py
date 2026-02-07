class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l=r=0
        min_len=10**5
        s_index=-1
        n=len(s)
        count=0

        freq={}
        
        for i in t:
            freq[i]= freq.get(i, 0) + 1
        while r<n:
            if s[r] in freq :
                if freq[s[r]]>0:
                    count+=1
                freq[s[r]]-=1
            
            
            while count==len(t):
                if (r-l+1)<min_len:
                    min_len=r-l+1
                    s_index=l
                    
                if s[l] in freq:
                    freq[s[l]]+=1
                
                    if freq[s[l]]>0:
                        count-=1
                l+=1
            r+=1
        return "" if s_index==-1 else s[s_index:(s_index+min_len)]
         

            
        