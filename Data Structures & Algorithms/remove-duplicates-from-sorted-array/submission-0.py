class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0

        # iterate backwards (so the holes are unproblematic)
        for i in range(len(nums)-1, -1, -1):
            while i > 0 and i < len(nums) and nums[i] == nums[i-1]:
                del nums[i]
                i -= 1
            unique += 1

        return unique