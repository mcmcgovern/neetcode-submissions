class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force: check every pair
        # optimized: compute difference of target - each num
        #   store these differences in a set
        #   if we encounter a previous diff as our current num, return

        diffs = {} # map diff:index
        for i, num in enumerate(nums):
            if num in diffs:
                return [diffs[num], i]

            diff = target - num
            diffs[diff] = i
