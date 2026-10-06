class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char={}
        l=0
        r=0
        maxlen=0
        n=len(s)
        while r<n:
            if s[r] not in char:
                char[s[r]]=1
            else:
                char[s[r]]+=1
            if ((r-l+1)-max(char.values()))<=k:
                maxlen=max(maxlen,r-l+1)
                r+=1
            else:
                if (r-l+1)-max(char.values())>k:
                    char[s[l]]-=1
                    l+=1
                maxlen=max(maxlen,r-l+1)
                r+=1
        return maxlen




    
        
        