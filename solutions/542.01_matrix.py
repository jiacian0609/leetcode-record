from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m == 1 and n == 1:
            return mat

        result = [[float('inf')] * n for _ in range(m)]
        q = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    q.append((i, j))

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            x, y = q.popleft()
            for dx, dy in dir:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and result[nx][ny] > result[x][y] + 1:
                    result[nx][ny] = result[x][y] + 1
                    q.append((nx, ny))

        return result