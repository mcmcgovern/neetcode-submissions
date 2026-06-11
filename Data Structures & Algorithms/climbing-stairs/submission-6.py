class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        seen = {0: 1, 1:1}
        i = 2
        while i <= n:
            seen[i] = seen[i-1] + seen[i-2]
            i += 1
        return seen[i-1]