class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1 if nums[0] == 1 else 0
        left = 0
        max_ones = 0

        while left < len(nums):
            if nums[left] == 1:
                right = left
                while right < len(nums) and nums[right] == 1:
                    right += 1
                max_ones = max(max_ones, right-left)
                left = right
            else:
                left += 1

        return max_ones