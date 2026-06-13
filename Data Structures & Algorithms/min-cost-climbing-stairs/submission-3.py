class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= len(cost)-2:
                dp[i] = cost[i]
                return dp[i]

            current_level = cost[i] + min(dfs(i+1), dfs(i+2))
            dp[i] = current_level
            return dp[i]

        return min(dfs(0), dfs(1))