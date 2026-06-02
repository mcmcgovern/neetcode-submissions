class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        longest = 1

        unique = set(nums)
        for num in unique:
            current_seq = 1
            next_element = num+1
            while next_element in unique:
                current_seq += 1
                next_element += 1
            longest = max(longest, current_seq)

        return longest