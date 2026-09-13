class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # range is 0 to n
        # n ints in nums
        unique = set(nums)
        for i in range(len(nums)):
            if i not in unique:
                return i
        return len(nums)