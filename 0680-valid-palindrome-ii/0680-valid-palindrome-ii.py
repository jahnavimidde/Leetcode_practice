class Solution(object):
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.check(left+1, right, s) or self.check(left, right-1, s)
        
        return True
    
    def check(self, left, right, s):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True