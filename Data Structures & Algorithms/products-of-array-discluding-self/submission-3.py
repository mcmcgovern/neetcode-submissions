class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix sum
        prefixes = [1] * len(nums) # 1,1,1,1
        for i in range(1, len(nums)):
            prefixes[i] *= prefixes[i-1] * nums[i-1]
        # 1, 1, 2, 4

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            prefixes[i] *= postfix
            postfix *= nums[i]
        return prefixes