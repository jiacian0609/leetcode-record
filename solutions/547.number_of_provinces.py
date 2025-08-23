class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()   # 紀錄已經拜訪過的城市
        provinces = 0     # 計算省份數（即連通分量）

        # 深度優先搜尋 (DFS)
        def dfs(city):
            visited.add(city)  # 標記當前城市為已拜訪
            # 檢查 city 這個城市跟哪些城市相連
            for cur, connected in enumerate(isConnected[city]):
                # connected = 1 表示 city 與 cur 相連
                # 如果相連且 cur 還沒被拜訪，繼續 DFS
                if connected and cur not in visited:
                    dfs(cur)
            
        # 逐一檢查每個城市
        for i in range(len(isConnected)):
            if i not in visited:   # 如果這個城市還沒拜訪過
                dfs(i)             # 從這個城市開始 DFS，找到一整個連通分量
                provinces += 1     # 省份數 +1

        return provinces
    
    def findCircleNumBFS(self, isConnected: List[List[int]]) -> int:
        visited = set()   # 紀錄已經拜訪過的城市
        provinces = 0     # 計算省份數（即連通分量）

        # 廣度優先搜尋 (BFS)
        def bfs(start):
            queue = deque([start])   # 建立 queue，起點放進去
            while queue:
                city = queue.popleft()   # 取出當前城市
                visited.add(city)        # 標記為已拜訪
                # 檢查 city 和哪些城市相連
                for cur, connected in enumerate(isConnected[city]):
                    # connected = 1 代表有連線，且 cur 未訪問過
                    if connected and cur not in visited:
                        queue.append(cur)   # 加入 queue，等待之後擴展
        
        # 逐一檢查每個城市
        for i in range(len(isConnected)):
            if i not in visited:   # 如果這個城市還沒拜訪過
                bfs(i)             # 用 BFS 把整個連通分量都跑完
                provinces += 1     # 省份數 +1
        
        return provinces