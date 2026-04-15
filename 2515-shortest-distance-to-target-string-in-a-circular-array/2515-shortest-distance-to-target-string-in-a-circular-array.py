class Solution(object):
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        ans = float('inf')

        for i in range(n):
            if words[i] == target:
                diff = abs(i - startIndex)
                ans = min(ans, min(diff, n - diff))

        return ans if ans != float('inf') else -1