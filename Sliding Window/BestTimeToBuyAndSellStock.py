#TC: O(n)
#SC: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        maxProfit = 0

        while i <= j and j < len(prices):
            profit = prices[j] - prices[i]
            
            if profit < 0:
                i += 1
            else:
                maxProfit = max(profit, maxProfit)
                j += 1
        
        return maxProfit