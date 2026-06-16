class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        for key, val in counts.items():
            if val > 1:
                return key
        return -1