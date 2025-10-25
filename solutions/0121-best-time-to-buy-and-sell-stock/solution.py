class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = prices[0]
        proits=[]
        for i in prices:
            if  i < mini:
                mini=i
            profit = i-mini
            proits.append(profit)
        return max(proits)
