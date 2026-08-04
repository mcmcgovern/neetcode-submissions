class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        # sliding window
        left, right = 0, 1
        while left < len(prices)-1:
            if right >= len(prices) or prices[left] > prices[right]:
                left += 1
                right = left + 1
            else:
                profit = prices[right] - prices[left]
                maxp = max(maxp, profit)
                right += 1
        return maxp