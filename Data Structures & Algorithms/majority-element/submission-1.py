
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
                if counts[num] > len(nums) // 2:
                    return num
            else:
                counts[num] = 1