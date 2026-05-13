class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        min_sell = prices[0]

        for sell in prices:
            max_p = max(max_p, sell - min_sell)
            min_sell = min(min_sell, sell)

        return max_p