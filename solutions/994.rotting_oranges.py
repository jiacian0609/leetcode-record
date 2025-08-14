from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        q = deque()
        next_q = deque()
        remaining = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    # print((i, j))
                    q.append((i, j))
                elif grid[i][j] == 1:
                    remaining += 1
        if remaining == 0:
            return 0

        r = -1
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y = q.popleft()
            for dx, dy in dir:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    next_q.append((nx, ny))
                    remaining -= 1
            if not q:
                r += 1
                q = next_q
                next_q = deque()

        return r if remaining == 0 else -1