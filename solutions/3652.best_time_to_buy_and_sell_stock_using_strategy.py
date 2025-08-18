class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        profit = sum(p * s for p, s in zip(prices, strategy))
        print(profit)

        new_profit = profit
        for i in range(k):  # modify first k element
            new_profit -= prices[i] * strategy[i]
            if i >= k // 2:
                new_profit += prices[i]
        print(0, new_profit)
        
        if new_profit > profit:
            profit = new_profit

        # sliding window
        for i in range(len(prices) - k):
            # 0 -> ori
            new_profit += prices[i] * strategy[i]
            # 1 -> 0
            new_profit -= prices[i + k // 2]
            # ori -> 1
            new_profit -= prices[i + k] * strategy[i + k]
            new_profit += prices[i + k] 
            print(i + 1, new_profit)

            if new_profit > profit:
                profit = new_profit

        return profit