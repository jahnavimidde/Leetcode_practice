class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        sec=[0]*len(bank)

        for r in range(len(bank)):
            for i in range(len(bank[r])):
                if bank[r][i]=='1':
                    sec[r]+=1
        ans=0       
        for r1 in range(len(sec)-1,-1,-1):
            for r2 in range(r1-1,-1,-1):
                
                    for i in range(r2+1,r1):
                      if sec[i]!=0:
                        break
                    else:
                        if sec[r1] != 0 and sec[r2] != 0:
                            ans+=sec[r1]*sec[r2] 

        return ans 
                    
                    
                
                
                
                
            
                
        
