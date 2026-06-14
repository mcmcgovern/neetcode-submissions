class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find partition, do binary search
        for index, num in enumerate(nums):
            if num == target:
                return index
        return -1