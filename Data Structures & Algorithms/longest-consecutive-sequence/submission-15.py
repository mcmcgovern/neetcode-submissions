class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find numbers that start a sequence
        # that is num-1 is not in nums
        unique = set(nums)
        longest = 0
        for num in nums:
            if num-1 in unique:
                continue
            else:
                # keep counting up to measure length of current sequence
                length = 0
                i = 0
                while num+i in unique:
                    length += 1
                    i += 1
                longest = max(length, longest)
        return longest