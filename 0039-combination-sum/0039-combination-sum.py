class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []
        self.helper(0, candidates, target, [], ans)
        return ans

    def helper(self, ind, candidates, target, ds, ans):
        # base condition
        if ind == len(candidates):
            if target == 0:
                ans.append(list(ds))
            return
        
        # pick
        if candidates[ind] <= target:
            ds.append(candidates[ind])
            self.helper(ind, candidates, target - candidates[ind], ds, ans)
            ds.pop()  # backtrack
        
        # not pick
        self.helper(ind + 1, candidates, target, ds, ans)
