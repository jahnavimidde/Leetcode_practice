class Solution:
    def minFlips(self, s):
        n = len(s)
        s = s + s
        
        cnt1 = 0
        cnt2 = 0
        ans = float('inf')
        
        for i in range(len(s)):
            
            if s[i] != str(i % 2):
                cnt1 += 1
            
            if s[i] != str((i + 1) % 2):
                cnt2 += 1
            
            if i >= n and s[i-n] != str((i-n) % 2):
                cnt1 -= 1
            
            if i >= n and s[i-n] != str((i + 1 - n) % 2):
                cnt2 -= 1
            
            if i >= n - 1:
                ans = min(ans, cnt1, cnt2)
        
        return ans