class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, char in enumerate(s):
            ans += (i + 1) * (26 - (ord(char) - ord('a')))

        return ans