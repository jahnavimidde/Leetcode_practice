class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ind=0
        ds=[]
        ans=[]
        result=self.helper(ind,ds,ans,s)
        return result
    def helper(self,ind,ds,ans,s):
        if ind==len(s):
            ans.append(ds[:])
            return
         
        for i in range(ind,len(s)):
            if self.ispalindrome(ind,i,s):
                ds.append(s[ind:i+1])
                self.helper(i+1,ds,ans,s)
                ds.pop()
        return ans
    def ispalindrome(self,ind,i,s):
        while ind<i:
            if s[ind]==s[i]:
                ind+=1
                i-=1
            else:
                return False
        return True
    

        


        