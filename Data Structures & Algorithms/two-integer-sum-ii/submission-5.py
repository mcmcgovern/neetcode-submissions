class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Since the array is sorted, we can use two pointers starting at both
        #   ends of the array and advance inward if we are too big / too small

        left, right = 0, len(numbers)-1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left+1, right+1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1