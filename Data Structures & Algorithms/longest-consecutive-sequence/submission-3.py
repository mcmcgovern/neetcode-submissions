class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # build a set with all values, check to see if next element is in set
        values = set()
        for num in nums:
            values.add(num)

        longest = 0
        for num in values:
            current = 1
            while num + 1 in values:
                current += 1
                num += 1
            longest = max(longest, current)
        return longest