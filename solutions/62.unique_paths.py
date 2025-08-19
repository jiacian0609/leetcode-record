class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1

        top = 1
        for i in range(m):
            top *= (m + n - i)
        
        bottom = 1
        for i in range(m):
            bottom *= (m - i)

        # print(top, bottom)
        return top // bottom