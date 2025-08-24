class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque([(entrance, 0)])
        visited = set()
        visited.add((entrance[0], entrance[1]))
        start = False
        while q:
            cur, step = q.popleft()
            x, y = cur[0], cur[1]
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if maze[nx][ny] == '.' and (nx, ny) not in visited:
                        q.append(([nx, ny], step + 1))
                        visited.add((nx, ny))
                elif start:
                    # print("end")
                    return step
            start = True
        return -1