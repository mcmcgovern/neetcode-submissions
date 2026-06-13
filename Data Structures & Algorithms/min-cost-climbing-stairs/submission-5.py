class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = cost[-2], cost[-1]
        for i in range(len(cost)-3, -1, -1):
            first, second = cost[i] + min(first, second), first
        return min(first, second)