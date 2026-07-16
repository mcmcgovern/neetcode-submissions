class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # try to implement trivial division soln
        result = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j and nums[i] == 0:
                    continue
                product *= nums[j]
            if nums[i] != 0:
                product //= nums[i]
            result.append(product)
        return result