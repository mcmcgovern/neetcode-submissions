class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # using sort
        nums.sort()
        # [2,3,4,4,5,10,20]

        longest = 1
        length = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                length += 1
                longest = max(longest, length)
            elif nums[i] == nums[i-1]:
                continue
            else:
                length = 1
        return longest