class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque()
        for s in senate:
            q.append(s)
        while len(set(q)) > 1:
            cur = q.popleft()
            opp = 'R' if cur == 'D' else 'D'
            if opp in q:
                q.remove(opp)
            q.append(cur)
        return "Radiant" if q[0] == 'R' else "Dire"