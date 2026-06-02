class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # two pointers
        max_profit = 0
        buy, sell = 0, 1
        while sell < len(prices):
            max_profit = max(max_profit, prices[sell] - prices[buy])
            if prices[sell] < prices[buy]:
                buy = sell
            
            sell += 1
        return max_profit


















        # # find first and second min
        # smallest, second_smallest = 101,101
        # for price in prices:
        #     if price < smallest:
        #         second_smallest = smallest
        #         smallest = price
        #     elif price == smallest:
        #         second_smallest = smallest

        # print(smallest, second_smallest)

        # if prices[len(prices)-1] == smallest:
        #     smallest = second_smallest

        # # next find largest after smallest
        # start = False
        # highest_considered = smallest
        # for price in prices:
        #     if price == smallest:
        #         start = True
        #     if start and price > highest_considered:
        #         highest_considered = price

        # return highest_considered - smallest

        



















        # brute force
        # result = 0
        # for i in range(0, len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         result = max(result, profit)

        # return result


"""
brute force
-do every combination
-double for loop
-n squared

two pass
-find min value
-find max value after that min
"""