class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profits=[]
        for i in range(len(prices)-1):
            dif=prices[i+1]-prices[i]
            if dif > 0:
                profits.append(dif)
        return sum(profits)
