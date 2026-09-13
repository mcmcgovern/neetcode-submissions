class Solution:
    def hammingWeight(self, n: int) -> int:
        counts = Counter(bin(n)[2:])
        return counts['1']
