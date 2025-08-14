from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        island_count = 0

        def bfs(i, j):
            q = deque([(i, j)])
            grid[i][j] = "0"  # 標記為訪問
            
            dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while q:
                x, y = q.popleft()
                for dx, dy in dir:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        q.append((nx, ny))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    island_count += 1

        return island_count