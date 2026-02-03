class Solution(object):
    def characterReplacement(self, s, k):
        hash = {}
        max_fre = 0
        max_len = 0
        l = 0

        for r in range(len(s)):
            hash[s[r]] = hash.get(s[r], 0) + 1
            max_fre = max(max_fre, hash[s[r]])

            if (r - l + 1) - max_fre > k:
                hash[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len