class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        start_x, start_y = 0, 0
        end_x, end_y = m - 1, n - 1

        # 如果可以瞬移一次且起點格 >= 終點格，直接瞬移到終點，花費 0
        if k > 0 and grid[start_x][start_y] >= grid[end_x][end_y]:
            return 0

        # dp[i][j] = 到達 (i,j) 的最小花費
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = 0

        # ------------------------------
        # Step 1: 計算沒有瞬移時的最短路徑 (只能往右或往下)
        # ------------------------------
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])

        # ------------------------------
        # Step 2: 處理瞬移 (最多使用 k 次)
        # 瞬移規則：可以從當前格子瞬移到任何值 <= 當前格子的格子，花費 0
        # ------------------------------
        for teleport_used in range(k):
            # 將格子按 -grid 值排序 (值大的格子在前面)
            # 因為可以從大格子瞬移到小格子
            cells_sorted = sorted(
                [(-grid[i][j], dp[i][j], i, j) for i in range(m) for j in range(n)]
            )

            # dp_next = 使用一次瞬移後的最小花費
            dp_next = [[float('inf')] * n for _ in range(m)]
            min_cost_so_far = float('inf')

            # 遍歷排序後的格子，模擬瞬移效果
            for _, current_cost, i, j in cells_sorted:
                # 取目前能瞬移到的最小 cost
                min_cost_so_far = min(min_cost_so_far, current_cost)
                dp_next[i][j] = min_cost_so_far

            # ------------------------------
            # Step 3: 瞬移後還能繼續走右/下
            # ------------------------------
            for i in range(m):
                for j in range(n):
                    if i == 0 and j == 0:
                        dp_next[i][j] = 0
                    else:
                        if i > 0:
                            dp_next[i][j] = min(dp_next[i][j], dp_next[i-1][j] + grid[i][j])
                        if j > 0:
                            dp_next[i][j] = min(dp_next[i][j], dp_next[i][j-1] + grid[i][j])
            
            # 更新 dp = 使用 teleport_used + 1 次瞬移後的最小花費
            dp = dp_next

        # 最終右下角的值就是答案
        return dp[-1][-1]
