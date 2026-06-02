class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = [num*num for num in nums]
        return sorted(squared)