class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # start from the end, modify cost in place
        # we know the last two values are both within range of finishing, so len-2
        for i in range(len(cost)-3, -1, -1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])