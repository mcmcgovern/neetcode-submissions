class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for bin_digit in bin(n)[2:]:
            if bin_digit == '1':
                count += 1
        return count
