class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        i = 0
        buy = 0
        n = len(prices)
        
        for i in range(len(prices)-1):
            diff = max(prices[i+1:n]) - prices[i]
            print(prices[i], max(prices[i+1:n]))

            profit = max(profit, diff)
        return profit 
            


        