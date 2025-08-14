class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        
        INF = amount + 1
        coins_need = [INF] * (amount + 1)
        coins_need[0] = 0

        for a in range(1, amount + 1):
            # print(a)
            for c in coins:
                if c <= a:
                    # print(a - c)
                    coins_need[a] = min(coins_need[a], coins_need[a - c] + 1)
                else:
                    break
                
            # print(coins_need)


        return coins_need[amount] if coins_need[amount] != INF else -1