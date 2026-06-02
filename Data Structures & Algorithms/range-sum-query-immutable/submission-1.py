class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = []
        total = 0
        for num in nums:
            total += num
            self.prefix_sums.append(total)
        

    def sumRange(self, left: int, right: int) -> int: 
        # get the left, get the right, subtract
        right_sum = self.prefix_sums[right]
        left_sum = self.prefix_sums[left - 1] if left > 0 else 0
        return right_sum - left_sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)