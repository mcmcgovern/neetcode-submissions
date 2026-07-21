class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # The idea is that we sum the values of our two pointers
        # If the sum > target, adjust right pointer, else adjust left
        left, right = 0, len(numbers)-1

        while left < right:
            pointer_sum = numbers[left] + numbers[right]
            if target == pointer_sum:
                return [left+1, right+1]
            elif target < pointer_sum:
                right -= 1
            else:
                left += 1
        return [-1,-1]