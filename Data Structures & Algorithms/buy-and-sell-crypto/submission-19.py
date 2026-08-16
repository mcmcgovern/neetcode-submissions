class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0
        left = 0
        for right, price in enumerate(prices):
            if price < prices[left]:
                left = right
            profit = price - prices[left]
            current_max = max(current_max, profit)
        return current_max