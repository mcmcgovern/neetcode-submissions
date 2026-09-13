class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # use sum
        actual_sum = sum(nums)
        r = [i for i in range(len(nums)+1)]
        complete_sum = sum(r)
        return complete_sum - actual_sum