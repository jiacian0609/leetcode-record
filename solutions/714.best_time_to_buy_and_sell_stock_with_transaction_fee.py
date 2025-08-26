class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 狀態定義：
        # buy  = 目前持有股票時的最大利潤
        # sell = 目前沒有股票時的最大利潤

        buy = float('-inf')  # 初始化為 -∞，代表一開始不可能持有股票
        sell = 0             # 一開始沒有股票，利潤是 0

        for price in prices:
            # 狀態轉移 1: 今天決定買入 or 不動作
            # - 不動作：保持昨天的 buy
            # - 今天買：昨天必須是 sell，今天花 price 買入 → sell - price
            buy = max(buy, sell - price)

            # 狀態轉移 2: 今天決定賣出 or 不動作
            # - 不動作：保持昨天的 sell
            # - 今天賣：昨天必須是 buy，今天以 price 賣出 → buy + price - fee
            sell = max(sell, buy + price - fee)

        # 最後答案一定是 sell (手上沒股票時才是最終最大利潤)
        return sell