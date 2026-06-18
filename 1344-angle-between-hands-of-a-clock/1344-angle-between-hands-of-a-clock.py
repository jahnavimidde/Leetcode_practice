class Solution(object):
    def angleClock(self, hour, minutes):
        # Angle made by minute hand
        minute_angle = minutes * 6

        # Angle made by hour hand
        hour_angle = (hour % 12) * 30 + minutes * 0.5

        # Difference between the two angles
        diff = abs(hour_angle - minute_angle)

        # Return the smaller angle
        return min(diff, 360 - diff)