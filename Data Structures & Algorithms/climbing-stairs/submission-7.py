class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one_before = 0
        two_before = 1
        i = 2
        while i <= n+1:
            temp = two_before
            two_before = one_before + two_before
            one_before = temp
            i += 1
        return two_before