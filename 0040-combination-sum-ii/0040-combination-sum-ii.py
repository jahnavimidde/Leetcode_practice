class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        self.helper(0, candidates, target, [], ans)
        return ans

    def helper(self, ind, candidates, target, ds, ans):
        if target == 0:
            ans.append(list(ds))
            return

        for i in range(ind, len(candidates)):
            # skip duplicates at same level
            if i > ind and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > target:
                break

            ds.append(candidates[i])
            self.helper(i + 1, candidates, target - candidates[i], ds, ans)
            ds.pop()
