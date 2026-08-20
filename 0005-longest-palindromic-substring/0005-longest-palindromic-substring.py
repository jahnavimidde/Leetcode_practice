class Solution(object):
    def longestPalindrome(self, s):

        def helper(left, right):
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            
            return s[left + 1:right]

        ans = ""

        for i in range(len(s)):

            # Odd length palindrome
            p1 = helper(i, i)

            # Even length palindrome
            p2 = helper(i, i + 1)

            if len(p1) > len(ans):
                ans = p1

            if len(p2) > len(ans):
                ans = p2

        return ans