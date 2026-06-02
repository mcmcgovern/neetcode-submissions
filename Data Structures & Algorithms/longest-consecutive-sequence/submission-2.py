class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        longest = 1

        unique = set(nums)
        seq_starts = set()
        for num in nums:
            if num-1 not in unique:
                seq_starts.add(num)

        for starting_num in seq_starts:
            current_element = starting_num
            current_length = 1
            while current_element+1 in unique:
                current_length += 1
                current_element += 1
            longest = max(longest, current_length)

        return longest