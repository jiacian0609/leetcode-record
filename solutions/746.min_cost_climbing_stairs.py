class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        min_cost = [float(inf)] * (n + 1)
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]

        for i in range(2, n + 1):
            min_cost[i] = min(min_cost[i - 1], min_cost[i - 2])
            if i < n:
                min_cost[i] += cost[i]
        
        return min_cost[-1]