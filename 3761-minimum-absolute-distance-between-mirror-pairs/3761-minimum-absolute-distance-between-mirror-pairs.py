import bisect

class Solution(object):
    def minMirrorPairDistance(self, nums):
        mp = {}

        # store indices
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]].append(i)
            else:
                mp[nums[i]] = [i]

        mini = float('inf')

        for i in range(len(nums)):
            rev = int(str(nums[i])[::-1])

            if rev in mp:
                lst = mp[rev]

                # find first index strictly greater than i
                pos = bisect.bisect_right(lst, i)

                if pos < len(lst):
                    mini = min(mini, lst[pos] - i)

        return mini if mini != float('inf') else -1