class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        cost=sorted(cost,reverse=True)
        if len(cost)<=2:
            return sum(cost)
        elif len(cost)==3:
            return sum(cost[0:2])
        else:
            extra=len(cost)%3
            loop=len(cost)-extra
            loop1=len(cost)//3
            i=2
            sum_free=0
            while loop1>0:
                
                
                sum_free+=cost[i]
                loop1-=1
                i+=3
            
        buy_sum=sum(cost)-sum_free
        return buy_sum      



        