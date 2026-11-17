class Solution(object):
    def topKFrequent(self, nums, k):
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1

        return sorted(d, key=lambda x: d[x], reverse=True)[:k]