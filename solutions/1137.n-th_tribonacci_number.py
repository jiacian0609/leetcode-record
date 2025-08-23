class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        num = [0] * (n + 1)
        num[1] = 1
        num[2] = 1
        
        if n >= 3:
            for i in range(3, n + 1):
                num[i] = num[i - 1] + num[i - 2] + num[i - 3]

        return num[-1]