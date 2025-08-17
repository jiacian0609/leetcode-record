import heapq
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        INF = float('inf')
        graph = [[] for _ in range(n)]
        
        for from_node, to_node, cost in edges:
            graph[from_node].append((to_node, cost))
            graph[to_node].append((from_node, cost * 2))
        
        d = [INF] * n  # 去各點的最短距離
        d[0] = 0
        q = [(0, 0)]
        
        while q:
            distance, from_node = heapq.heappop(q)  # pop 出 heap 裡最近的
            if distance > d[from_node]:  # 先前的距離更短，不用更新
                continue
            
            for to_node, cost in graph[from_node]:
                if d[to_node] > d[from_node] + cost:
                    d[to_node] = d[from_node] + cost
                    heapq.heappush(q, (d[to_node], to_node))
        
        return -1 if d[n - 1] == INF else d[n - 1]