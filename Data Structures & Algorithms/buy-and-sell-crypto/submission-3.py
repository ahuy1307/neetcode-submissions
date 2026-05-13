class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_sell = prices[0]
        max_p = 0
        
        for price in prices:
            max_p = max(max_p, price - min_sell)
            min_sell = min(min_sell, price)

        return max_p