class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix sum -> prefix product
        product_so_far = nums[0]
        products = [1] * len(nums)
        for i in range(1, len(nums)):
            products[i] *= product_so_far
            product_so_far *= nums[i]

        product_so_far = 1
        for i in range(len(nums)-2, -1, -1):
            product_so_far *= nums[i+1]
            products[i] *= product_so_far

        return products