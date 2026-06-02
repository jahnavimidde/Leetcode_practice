class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        minFinishTime = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                # Option 1: Land ride first, then water ride
                land_start = landStartTime[i]
                land_end = land_start + landDuration[i]
                water_start = max(land_end, waterStartTime[j])
                finish1 = water_start + waterDuration[j]

                # Option 2: Water ride first, then land ride
                water_start2 = waterStartTime[j]
                water_end = water_start2 + waterDuration[j]
                land_start2 = max(water_end, landStartTime[i])
                finish2 = land_start2 + landDuration[i]

                # Take the minimum of both orders
                minFinishTime = min(minFinishTime, finish1, finish2)

        return minFinishTime
