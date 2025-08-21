class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        cur = 0
        for g in gain:
            cur += g
            if cur > max_altitude:
                max_altitude = cur
        return max_altitude