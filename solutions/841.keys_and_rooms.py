class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        num = len(rooms)
        visited = [False] * num
        visited[0] = True

        q = deque([0])
        while q:
            cur = q.popleft()
            neighbors = rooms[cur]
            for nei in neighbors:
                if not visited[nei]:
                    q.append(nei)
                    visited[nei] = True

        return all(v for v in visited)