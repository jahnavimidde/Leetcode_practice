class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_count=Counter(p)
        window=Counter()
        left=0
        right=0
        ans=[]
        while right<=len(s)-1:
            window[s[right]]+=1
            while right-left+1>len(p):
                window[s[left]]-=1
                if window[s[left]]==0:
                    del window[s[left]]
                left+=1
            if window==p_count:
                ans.append(left)
            right+=1
        return ans



                
        