class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        # first let's do brute force
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit = prices[j] - prices[i]
                maxp = max(maxp, profit)
        return maxp