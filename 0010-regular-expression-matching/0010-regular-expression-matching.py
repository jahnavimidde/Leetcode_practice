class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            if j == len(p):
                return i == len(s)

            if (i, j) in memo:
                return memo[(i, j)]

            first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                ans = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                ans = first_match and dfs(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dfs(0, 0)