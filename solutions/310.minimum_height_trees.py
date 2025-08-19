from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 特殊情況：如果只有一個節點，直接返回它
        if n == 1:
            return [0]

        # 1️⃣ 建立鄰接表 graph
        # graph[node] = set(鄰居節點)
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # 2️⃣ 找出初始葉子節點
        # 葉子節點的特徵：只有一個鄰居
        leaves = [i for i in range(n) if len(graph[i]) == 1]

        # 3️⃣ 開始剝葉子
        remaining_nodes = n
        while remaining_nodes > 2:  # 最小高度樹最多只有 2 個根
            remaining_nodes -= len(leaves)  # 每次剝掉的葉子數量
            new_leaves = []  # 新一輪葉子節點

            for leaf in leaves:
                # 由於葉子只有一個鄰居，取出它
                neighbor = graph[leaf].pop()
                # 把葉子從鄰居的集合裡移除
                graph[neighbor].remove(leaf)

                # 如果鄰居變成葉子，就加入新葉子列表
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # 更新葉子列表，進入下一輪
            leaves = new_leaves

        # 4️⃣ 剩下 1 或 2 個節點就是最小高度樹的根
        return leaves