class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        i, j = 0, 0
        n = len(grid)
        count = 0
        for i in range(n):
            for j in range(n):
                match = False
                for k in range(n):
                    if grid[i][k] == grid[k][j]:
                        if k == n - 1:
                            match = True
                        continue
                    else:
                        break
                if match:
                    count += 1
        return count