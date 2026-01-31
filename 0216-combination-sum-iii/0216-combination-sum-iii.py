class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        start=1
        ds=[]
        ans=[]
        target=n
        
        result=self.helper(start,ds,target,k,ans)
        return result
    def helper(self,start,ds,target,k,ans):
        if len(ds)==k:
            if target==0:
                ans.append(ds[:])

            return 
        for i in range(start,10):
            if i>target:
                break
            ds.append(i)
            self.helper(i+1,ds,target-i,k,ans)
            ds.pop()
        return ans 
        
        
        