class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # range is 0 to n
        # n ints in nums
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)