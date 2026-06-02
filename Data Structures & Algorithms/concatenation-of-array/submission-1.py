class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # probs uneccessary, initialize array
        ans = 2 * len(nums) * [0]

        # two passes
        current = 0
        for i in range (len(nums)):
            ans[current] = nums[i]
            current += 1

        for i in range (len(nums)):
            ans[current] = nums[i]
            current += 1

        return ans