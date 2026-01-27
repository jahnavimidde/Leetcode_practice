class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=self.helper(n,0,0,"",[])
        return ans 
    def helper(self,n,open_,close,para,res):
        if open_==close==n:
            res.append(para)
        if open_<n:
            self.helper(n,open_+1,close,para+"(",res)
        if close<open_:
            self.helper(n,open_,close+1,para+")",res)
        return res 

        