class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # probs uneccessary, initialize array
        ans = 2 * len(nums) * [0]

        # one pass
        for i in range (len(nums)):
            ans[i] = ans[len(nums)+i] = nums[i]

        return ans