class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one_before = 0
        two_before = 1
        for i in range(n):
            two_before, one_before = one_before + two_before, two_before
        return two_before