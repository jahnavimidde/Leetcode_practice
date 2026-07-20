class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
    
        text1=str1
        text2=str2
        n, m = len(text1), len(text2)

        
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        
        i, j = n, m
        lcs=""

        
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                lcs+=text1[i-1]
                i-=1
                j-=1

                
                
                
            elif dp[i - 1][j] > dp[i][j - 1]:
                
                lcs+=str1[i-1]    #or take str2[j-1] not take str1[i-1]
                i-=1

                
            else:
                
                lcs+=str2[j-1]  #or take str2[j-1] not take str1[i-1]
                j-=1
        while i > 0:
            lcs += str1[i-1]
            i -= 1

        while j > 0:
            lcs += str2[j-1]
            j -= 1
        
        return lcs[::-1]
        
        
            



    

        
            
        

        
        





        
            
            
        
        