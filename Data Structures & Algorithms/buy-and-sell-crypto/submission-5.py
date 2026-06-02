class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0
        i = 0
        for j in range(1, len(prices)):
            if prices[j] > prices[i]:
                current_max = max(current_max, prices[j] - prices[i])
            else:
                i = j
        return current_max