class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        current_max = 0
        left, right = 0, 1
        while left < len(prices) - 1:
            # guard against right out of bounds
            if right == len(prices) or prices[right] < prices[left]:
                left += 1
                right = left
            else:
                current_max = max(current_max, prices[right] - prices[left])
                right += 1
        return current_max