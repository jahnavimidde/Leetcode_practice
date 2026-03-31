class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        count=Counter()
        left=0
        right=0
        maxi=0
        w_size=0
        while right<=len(fruits)-1:
            count[fruits[right]]+=1
            
            
            
            while len(count)>2:
                
                count[fruits[left]] -= 1
                if count[fruits[left]]==0:
                    del count[fruits[left]]
                left+=1
            if len(count)<=2:
                maxi=max(right-left+1,maxi)


            
            
            right+=1
        return maxi 
                
