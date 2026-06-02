class Solution:
    seen = { 1: 1 }
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        one_stair, two_stairs = 0, 0

        if n-1 in self.seen:
            one_stair = self.seen[n-1]
        else:
            self.seen[n-1] = self.climbStairs(n-1)

        if n-2 in self.seen:
            two_stairs = self.seen[n-2]
        else:
            self.seen[n-2] = self.climbStairs(n-2)

        return self.seen[n-1] + self.seen[n-2]