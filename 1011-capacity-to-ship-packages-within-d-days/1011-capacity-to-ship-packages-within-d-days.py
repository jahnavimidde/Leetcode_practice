class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        l=max(weights)
        h=sum(weights)
        
        while l<=h:
            mid=(l+h)//2

            days_need=1
            current=0
            for w in weights:
                if w+current>mid:
                    days_need+=1
                    current=0
                current+=w
            if days_need<=days:
                ans=mid
                h=mid-1
            
            else:
                l=mid+1
        return ans
                
                
                

        
        