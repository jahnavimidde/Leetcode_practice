from bisect import bisect_right


class Solution:
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):

        def solve(start1, dur1, start2, dur2):

            rides = sorted(zip(start2, dur2))
            starts = [s for s, d in rides]

            n = len(rides)

            # prefix minimum duration
            pref = [0] * n
            pref[0] = rides[0][1]

            for i in range(1, n):
                pref[i] = min(pref[i - 1], rides[i][1])

            # suffix minimum (start + duration)
            suff = [0] * n
            suff[-1] = rides[-1][0] + rides[-1][1]

            for i in range(n - 2, -1, -1):
                suff[i] = min(
                    suff[i + 1],
                    rides[i][0] + rides[i][1]
                )

            ans = float('inf')

            for s1, d1 in zip(start1, dur1):

                finish1 = s1 + d1

                # last index with start <= finish1
                pos = bisect_right(starts, finish1)

                cur = float('inf')

                # rides already open
                if pos > 0:
                    cur = min(cur, finish1 + pref[pos - 1])

                # rides not yet open
                if pos < n:
                    cur = min(cur, suff[pos])

                ans = min(ans, cur)

            return ans

        land_to_water = solve(
            landStartTime,
            landDuration,
            waterStartTime,
            waterDuration
        )

        water_to_land = solve(
            waterStartTime,
            waterDuration,
            landStartTime,
            landDuration
        )

        return min(land_to_water, water_to_land)