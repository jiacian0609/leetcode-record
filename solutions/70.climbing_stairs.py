class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        prev_1 = 3
        prev_2 = 2
        tot = 0
        
        for _ in range(3, n):
            tot = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = tot

        return tot
        