class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the array starts out in sorted order, though it has been rotated
        # rotating the array x times moves the last x elements to the front
        # all nums are unique
        return min(nums)