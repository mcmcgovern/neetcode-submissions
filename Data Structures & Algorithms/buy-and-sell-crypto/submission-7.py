class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        left, right = 0, 1

        current_max = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            current_max = max(current_max, profit)

            if prices[right] < prices[left]:
                left = right
            else:
                right += 1
        return current_max