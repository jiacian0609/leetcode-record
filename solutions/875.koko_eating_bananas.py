import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calHour(piles, speed):
            hour = 0
            for num in piles:
                hour += math.ceil(num / speed)
            return hour

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if calHour(piles, mid) <= h:
                right = mid   # 可以吃完 → 嘗試更小的速度
            else:
                left = mid + 1  # 吃不完 → 需要更快
        return left