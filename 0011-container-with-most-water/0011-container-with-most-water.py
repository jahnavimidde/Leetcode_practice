class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low=0
        high=len(height)-1
        maxwater=0
        while low<high:
            if height[low]<height[high]:
                maxwater=max(height[low]*(high-low),maxwater)
                low+=1

            elif height[low]>height[high]:
                maxwater=max(height[high]*(high-low),maxwater)
                high-=1
            else:
                maxwater=max(height[low]*(high-low),maxwater)
                low+=1

        return maxwater
            

            
        

            
        
        