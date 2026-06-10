class Solution:
    seen = {}
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        elif n in self.seen:
            return self.seen[n]
        
        self.seen[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.seen[n]