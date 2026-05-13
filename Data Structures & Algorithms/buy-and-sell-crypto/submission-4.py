class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_P = 0
        min_S = prices[0]

        for price in prices:
            max_P = max(max_P, price - min_S)
            min_S = min(min_S, price)

        return max_P