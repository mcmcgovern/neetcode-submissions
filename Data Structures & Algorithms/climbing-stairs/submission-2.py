class Solution:
    seen = { 1: 1 }
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        if n-1 not in self.seen:
            self.seen[n-1] = self.climbStairs(n-1)

        if n-2 not in self.seen:
            self.seen[n-2] = self.climbStairs(n-2)

        return self.seen[n-1] + self.seen[n-2]