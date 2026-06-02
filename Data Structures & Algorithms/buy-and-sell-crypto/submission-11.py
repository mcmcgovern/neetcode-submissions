class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        current_max = 0
        # use two pointers
        left, right = 0, 1
        while left < len(prices) - 1:
            if right == len(prices):
                left += 1
                right = left
            else:
                if prices[right] >= prices[left]:
                    current_max = max(current_max, prices[right] - prices[left])
                    right += 1
                else:
                    left += 1
                    right = left
        return current_max