class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in diffs:
                return sorted([i, diffs[difference]])
            else:
                diffs[num] = i

        return []