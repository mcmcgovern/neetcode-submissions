class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones_count = 0
        for char in s:
            if char == '1':
                ones_count += 1
        return (ones_count - 1) * '1' + (len(s) - ones_count) * '0' + '1'