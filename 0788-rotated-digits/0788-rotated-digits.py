class Solution(object):
    def rotatedDigits(self, n):
        count = 0
        
        for i in range(1, n + 1):
            s = str(i)
            
            
            if any(d in s for d in "347"):
                continue
            
           
            if any(d in s for d in "2569"):
                count += 1
                
        return count

           
        
        

        
                


        