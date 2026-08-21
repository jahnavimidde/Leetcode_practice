class Solution(object):
    def countSubstrings(self, s):

        def helper(left, right):
            count = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            return count

        ans = 0

        for i in range(len(s)):

            # Odd-length palindromes
            ans += helper(i, i)

            # Even-length palindromes
            ans += helper(i, i + 1)

        return ans