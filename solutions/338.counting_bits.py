class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ans = [0] * (n + 1)
        ans[1] = 1

        next_2 = 2
        for i in range(2, n + 1):
            if i == next_2:
                ans[i] = 1
                next_2 *= 2
            elif i % 2 == 0:
                ans[i] = ans[i // 2]
            else:
                ans[i] = ans[i - 1] + 1
        return ans