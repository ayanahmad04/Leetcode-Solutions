class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        forward = []
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
            forward.append(max_profit)
        max_price = prices[-1]
        backward = []
        for price in prices[::-1]:
            max_price = max(max_price, price)
            profit = max_price - price
            backward.append(profit)
        backward.reverse()
        best = []
        for item1, item2 in zip(forward, backward):
            best.append(item1 + item2)
        return (max(best))
