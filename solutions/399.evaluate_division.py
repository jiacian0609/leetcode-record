class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        neighbors = defaultdict(list)
        for (n1, n2), v in zip(equations, values):
            neighbors[n1].append((n2, v))
            neighbors[n2].append((n1, 1 / v))

        def dfs(start, end, cur_result):
            if start == end:
                return cur_result
            for nei, v in neighbors[start]:
                if nei in self.visited:
                    continue
                self.visited.add(nei)
                attempt = dfs(nei, end, cur_result * v)
                if attempt != -1:
                    return attempt
            return -1

        result = []
        for n1, n2 in queries:
            if n1 in neighbors and n2 in neighbors:
                self.visited = set([n1])  # 初始化 visited，從 n1 開始
                result.append(dfs(n1, n2, 1))
            else:
                result.append(-1)

        return result