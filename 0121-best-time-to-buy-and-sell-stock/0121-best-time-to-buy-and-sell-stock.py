class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0 

        left = 0 

        for i in range(1 ,len(prices)):

            if prices[i] < prices[left] : 
                left = i 

            else : 
                diff = prices[i] - prices[left]
                if diff > max_profit  :
                    max_profit  = diff

        return max_profit


