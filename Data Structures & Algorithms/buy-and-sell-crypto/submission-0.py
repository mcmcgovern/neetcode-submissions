class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # potential_max = 0

        # min_index, max_index = -1, -1
        # for i in range(len(prices)):
        #     if prices[i] < prices[min_index]:
        #         min_index = i
        #     if prices

        # return potential_max
        
        # brute force
        result = 0
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                result = max(result, profit)

        return result


"""
brute force
-do every combination
-double for loop
-n squared

two pass
-find min value
-find max value after that min
"""